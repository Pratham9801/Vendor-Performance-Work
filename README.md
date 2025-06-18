# **Vendor Performance Analysis Project**

### 📌 Project Overview

This end-to-end data analysis project analyzes vendor performance. The data is sourced from six CSV files:

1. `Vendor_invoice`
2. `Purchases`
3. `Sales`
4. `Purchase_Prices`
5. `End_Inventory`
6. `Begin_Inventory`

The project aims to assess vendor effectiveness through insights into purchase behavior, sales performance, inventory turnover, unit cost analysis, gross profit, and profit margins.

It involves:
- **Data ingestion** from large CSV files into a MySQL database
- **Data transformation** and aggregation
- **Exploratory data analysis (EDA)**
- **Statistical testing**
- **Power BI dashboarding** for insightful visualizations
- **Generating Final Report**

### 🎯 Business Objectives
- Spot weak brands
- Determine top vendors contributing to sales and gross profit 
- Analyze the impact of bulk purchasing on unit cost
- Asses inventory turnover to reduce holding costs and improve efficiency
- Investigate the profitability variance between high performing and low performing vendors

----

### 📁 Project Structure

#### 📜 Python Scripts
- `Ingestion_db.py`: Transfers raw CSV data into MySQL tables.
- `get_vendor_summary.py`: Performs data cleaning and preprocessing for analysis.
#### 📓 Jupyter Notebooks
1. **Exploratory_Data_Analysis.ipynb**: Performs SQL operations and initial data cleaning to select relevant columns aligned with the business questions.
2. **Vendor_Performance_Analysis.ipynb**: Contains the core analytical work, including statistical analysis, visualizations, and business insights.
#### 🧾 Additional Files
- `Logs/`: Contains logs for ingestion and preprocessing tasks
- `Vendor_Performance_Analysis.pbix`: Interactive dashboard summarizing key vendor metrics
- `Vendor_Performance_Analysis_Report.pdf`: Final report summarizing the findings.

----

### 🔍 Key Insights
- Identified top- and low-performing vendors based on sales and profit margins
- Detected brands needing promotional efforts or pricing adjustments
- Analyzed the impact of bulk order size on pricing and contribution
- Applied Pareto analysis for vendor contribution to total purchases  
----

### 🧰 Tools & Technologies
- Languages: Python
- Libraries: pandas, numpy, seaborn, matplotlib
- Database: MySQL
- Visualization: Power BI
- Platform: Jupyter Notebook
---

#### Data
Large datasets are excluded from the repository due to size constraints.

---

#### 📈 Power BI Dashboard

![image](https://github.com/user-attachments/assets/a4d6e8a5-85c5-40e9-98c5-a1d2b691e127)


[Click Here to see the Vendor Performance Dashboard](./Vendor_Performance_Project.pbix)

📌 **Note**: You’ll need [Power BI Desktop](https://powerbi.microsoft.com/desktop/) to open the above file.


   





