import pandas as pd
import sqlalchemy
import numpy as np
import logging 
from ingestion_db import ingest_db

logging.basicConfig(
   filename="logs/get_vendor_summary.log",
   level=logging.DEBUG,
   format="%(asctime)s- %(levelname)s- %(message)s",
   filemode='a'
   force=True

)

def create_vendor_summary(conn):
    '''this function will merge the different tables to get the overall vendor summary and adding new columns in resultant data '''
    vendor_sales_summary= pd.read_sql_query("""WITH FreightSummary as(
                select 
                   VendorNumber,
                   SUM(Freight) as FreightCost
                from vendor_invoice
                group by VendorNumber
                ),

                PurchaseSummary as (
                    select 
                        p.VendorNumber,
                        p.VendorName,
                        p.Brand,
                        p.Description,
                        p.PurchasePrice,
                        pp.Price as ActualPrice,
                        pp.Volume,
                        SUM(p.Quantity) as TotalPurchaseQuantity,
                        SUM(p.Dollars) as TotalPurchaseDollars
                    from purchases as p
                    JOIN purchase_prices pp
                        ON p.Brand=pp.Brand
                    where p.PurchasePrice > 0
                    GROUP BY p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice,pp.Price,pp.Volume
                ),

                    SalesSummary as (
                        select 
                            VendorNo,
                            Brand,
                            SUM(SalesQuantity) as TotalSalesQuantity,        
                            SUM(SalesPrice) as TotalSalesPrice,
                            SUM(SalesDollars) as TotalSalesDollars,
                            SUM(ExciseTax) as TotalExciseTax
                        from sales
                        group by VendorNo, Brand
                    )

                        select 
                            ps.VendorNumber,
                            ps.VendorName,
                            ps.Brand,
                            ps.Description,
                            ps.PurchasePrice,
                            ps.ActualPrice,
                            ps.Volume,
                            ps.TotalPurchaseQuantity,
                            ps.TotalPurchaseDollars,
                            ss.TotalSalesQuantity,
                            ss.TotalSalesDollars,
                            ss.TotalSalesPrice,
                            ss.TotalExciseTax,
                            fs.FreightCost
                        from PurchaseSummary ps
                        LEFT JOIN SalesSummary ss
                            on ps.VendorNumber=ss.VendorNo
                            and ps.Brand=ss.Brand
                        LEFT JOIN FreightSummary fs
                            on ps.VendorNumber = fs.VendorNumber
                        ORDER BY ps.TotalPurchaseDollars DESC
                        """,conn)
    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    #Changing datatype to float
    df['Volume']=df['Volume'].astype('float64')
    
    #filling missing values with 0
    df.fillna(0,inplace=True)
    
    #removing spces from categorical column 
    df['VendorName']=df['VendorName'].str.strip()
    df['Description']=df['Description'].str.strip()
    
    #Creating new columns for better analysis
    vendor_sales_summary['GrossProfit']=vendor_sales_summary['TotalSalesDollars']-vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin']=(vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalSalesDollars'])*100
    vendor_sales_summary['StockTurnover']=(vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity'])
    vendor_sales_summary['SalestoPurchaseRatio']=(vendor_sales_summary['TotalSalesDollars']/vendor_sales_summary['TotalPurchaseDollars'])
    
    vendor_sales_summary.replace([np.inf, -np.inf], np.nan, inplace=True)
    
    return df

if __name__=='__main__':
    #Creating datbase connection
    engine=sqlalchemy.create_engine("mysql+pymysql://root:root@localhost:3306/inventory")
    conn=engine.connect()
    
    logging.info("Creating Vendor Summary table ......")
    summary_df=create_vendor_summary(conn)
    logging.info(summary_df.head())
    
    logging.info("Cleaning the data  ......")
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())
    
    logging.info("Ingesting Data....")
    ingest_db(clean_df,'vendor_summary_table',conn)
    logging.info("Completed !!")
    
    
    