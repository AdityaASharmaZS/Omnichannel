# Databricks notebook source
# MAGIC %md
# MAGIC # NBA - Omnichannel Prediction Model
# MAGIC
# MAGIC The solution here aims to use AI/ML models to enhance NBA planning efficiency and effectiveness by leveraging machine learning techniques and comprehensive data analysis, and provide curated recommendation at a monthly/weekly level based on the types of constraints set.
# MAGIC
# MAGIC ## Solution Overview
# MAGIC Here we have create a ML model, which generates NBA predictions based on the input data and user input contraints from GUI.
# MAGIC 1) Quarterly Guardrails: Establishes guardrails at the quarter level, encompassing engagement goals, vendor contracts, and other constraints to guide NBA planning.
# MAGIC 2) Budget Optimization: Consolidates budgets for Integrated Promotional Planning (IPP) to optimize touchpoint volume recommendations at the HCP level.
# MAGIC 3) Temporal Adjustment: Converts HCP quarter recommendations into monthly recommendations using historical two-month actual promotion data.
# MAGIC 4) Optimal Touchpoint Distribution: Develops an optimal distribution and sequence of touchpoints utilizing decision tree-based models or other approaches to maximize effectiveness.
# MAGIC
# MAGIC
# MAGIC ## Data
# MAGIC Data Files include HCP Data including channel priority, historical hcp data, vendor contract and much more, which are all reference to generate NBA plan based on cadence date.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Notebooks and Scripts
# MAGIC
# MAGIC There is one Notebook and One Script in the package:
# MAGIC 1. Model Configurations: Notebook for configuring the environment manually using the variables.
# MAGIC 2. Model input parameters: Notebook containing the GUI for configuring the environment, and execute the model.
# MAGIC 3. Data Files Setup: Notebook to take the filePath from environment and create/update the Databricks Catalog with the tables required for model execution.
# MAGIC 4. Model Workflow: Notebook containing all the model functions and logic required for processing NBA.
# MAGIC 5. Model Orchestrator: Notebook to run the model workflow with a single execution.
# MAGIC 6. Dashboard setup instructions: This notebook lists all the steps required to detup the dashboard in the databricks environment.

# COMMAND ----------

# MAGIC %md
# MAGIC # Setup
# MAGIC If you are new to Databricks, create an account at: https://databricks.com/try-databricks
# MAGIC
# MAGIC ## Environment Setup
# MAGIC <ol><li> Create a Databricks Cluster with Databricks Compute 14.3 LTS.</li>
# MAGIC <li> Install the following libraries by going to your created cluster, and navigating to libraries tab:
# MAGIC   <ol><li> Click on "Install New".</li>
# MAGIC   <li> Navigate to PyPI.</li>
# MAGIC   <li> Pass the Librariy Names one ata time and install all the required libraries for setup.</li></ol></li></ol>
# MAGIC   
# MAGIC ### Libraries Required
# MAGIC 1. PyYAML
# MAGIC 2. gekko
# MAGIC 3. kaleido
# MAGIC 4. pyspark
