# Databricks notebook source
print('Hello World')

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello"

# COMMAND ----------

# MAGIC %fs ls 'databricks-datasets'

# COMMAND ----------

# MAGIC %md
# MAGIC # Convert to Delta table
# MAGIC spark.sql("CONVERT TO DELTA parquet.`dbfs:/user/hive/warehouse/dbaall.db/lkup_agmt_id_trnslt`")
# MAGIC
