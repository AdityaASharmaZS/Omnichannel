# Dashboards Setup Instructions

This Notebook will list all the steps and requirements necessary to import the dashboards in Azure databricks Environment.

# Requirements

## Functional Requirements
Your Azure Databricks should support SQL and Dashboards functionality (Azure databricks Premium.)

## Data Requirements
1. You should have access to model_performance, data_drift_table, and hcpo_weekly_plan files
2. Access to Dashboard json files.

# SQL Warehouse Setup

1. Go to Compute Tab in your Azure DataBricks Platform.
2. Navigate to SQL Warehouses tab.
3. Click on Create SQL Warehouse.
4. Name the cluster, and select cluster size as per compute requirements (Small in this case).
5. Click on Create.

# Data Import in Unity Catalog

1. Go to Data Ingestion within Data Engineering tab from you Databricks Menu.
2. Click on Create or Modify table
3. Either 'Drag and Drop' your files (in Data Requirements) or click on browse and select the required files (one by one)
4. Select the option "Create new Table" if it does not exist or overwrite existing table if table exists.
5. Click on Create(Overwrite) Table.
6. Repeat the process for all required Dashboard data files.

# Importing the Dashboards
The Dashboards should be imported after Data Import in Unity Catalog.

1. Go to Dashboards within SQl tab in your Databricks menu.
2. Click on dropdown Menu beside Create DashBoard Button.
3. Click on Import Dashboard from file.
4. Click on choose file.
5. Select the Dashboard json files from your local system.
6. Click on Import dashboard.
