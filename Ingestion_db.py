# sending data to database 
#importing pandas , os , sqlalchemy 


import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
   filename="logs/ingestion_db.log",
   level=logging.DEBUG,
   format="%(asctime)s- %(levelname)s- %(message)s",
   filemode='a'

)


#Create the engine
engine=create_engine('mysql+pymysql://root:root@localhost:3306/inventory')


#os.getcwd()    
folder_path='C:\\Users\\Prathamesh\\Vendor Performance Analysis'    #created the current folder path


def ingest_db(df,table_name,engine):
    '''this function will ingest the dataframe in the database with required tablename with help of connection established through engine'''
    df.to_sql(table_name,con=engine,if_exists='replace',index=False)
    
#if_exists='replace'	If a table with that name already exists: delete it and create a new one

def load_raw_data():
    '''this function will load the CSVs as Dataframes and ingest into database'''
    start=time.time()
    for file in os.listdir(folder_path):
        if '.csv' in file:
            file_path=os.path.join(folder_path,file)
            df=pd.read_csv(file_path)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time=(end-start)/60             #because it provides in seconds we need in minutes so divide by 60
    
    logging.info('-----------------Ingestion Complete------------------')
    logging.info(f'\nTotal time taken : {total_time} minutes')
    
if __name__=='__main__':
    load_raw_data()