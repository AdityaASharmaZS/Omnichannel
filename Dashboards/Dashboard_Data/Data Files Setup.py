# Databricks notebook source
import os

# COMMAND ----------

catalog_name = "non_prod_catalog"

# COMMAND ----------

schema_name = "dashboard_data"

# COMMAND ----------

# Set the Spark catalog to be used during the run
spark.sql(f"USE CATALOG {catalog_name}")

# COMMAND ----------

#Set the Files Schema to be used during the run
spark.catalog.setCurrentDatabase(f"{schema_name}")

# COMMAND ----------

def create_table_from_csv(file_path, table_name):
    if(file_path!=None):
        # Read the CSV file into a DataFrame
        print(os.path.abspath(file_path))
        file_path = os.path.abspath(file_path) 

        # Read the CSV file into a Spark DataFrame with inferred schema
        df_spark = (spark.read.format("csv")
                         .option("header", True)
                         .option("inferSchema", True)
                         .load(f"file://{file_path}"))

        col_names = [col_name.replace(" ", "_").replace(",", "").replace(";", "").replace("{", "").replace("}", "").replace("(", "").replace(")", "").replace("\n", "").replace("\t", "").replace("=", "") for col_name in df_spark.columns]
        df_spark = df_spark.toDF(*col_names)

        # Create or replace the table in Databricks
        spark.sql(f"DROP TABLE IF EXISTS {table_name}")
        df_spark.write.mode("overwrite").saveAsTable(table_name)
        print(f"Table '{table_name}' created successfully from file '{file_path}'")

# COMMAND ----------

create_table_from_csv('data_drift_table','data_drift_table')
create_table_from_csv('hcp_weekly_plan','hcp_weekly_plan')
create_table_from_csv('model_performance','model_performance')

# COMMAND ----------


