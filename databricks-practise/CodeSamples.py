# Databricks notebook source
dbutils.fs.help()

# COMMAND ----------

dbutils.fs.mount(
source = 'wasbs://raw@blobstrgtrp86.blob.core.windows.net/',
mount_point = '/mnt/raw/',
extra_configs = {'fs.azure.account.key.blobstrgtrp86.blob.core.windows.net':'O5RCSg41Bil39BpcNFTyg17AIK6C9YbbSRgOpOCS4TBs+DEeDCh5eUUED+NiCxa0wZj8CrdhSkfN+AStJYiXJA=='} 
)

# COMMAND ----------

dbutils.fs.ls ('/mnt/raw/')

# COMMAND ----------

df = spark.read.csv('/mnt/raw/', header = True)
display(df)
