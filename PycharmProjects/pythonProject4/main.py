import pyspark

## create spark session
spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL Example") \
    .config('spark.driver.extraClassPath', "/sqljdbc_12.4.1.0/jars/mssql-jdbc-12.4.1.jre8.jar") \
    .getOrCreate()

## read table [Production].[Product] from db
def extract_Product_to_df():
    Product_df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://;serverName=localhost;databaseName=AdventureWorks2022;integratedSecurity=true;encrypt=true;trustServerCertificate=true") \
        .option("dbtable", "[Production].[Product]") \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .load()
    return Product_df

def extract_WorkOrder_to_df():
## read table [Production].[WorkOrder] from db
    WorkOrder_df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://;serverName=localhost;databaseName=AdventureWorks2022;integratedSecurity=true;encrypt=true;trustServerCertificate=true") \
        .option("dbtable", "[Production].[WorkOrder]") \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .load()
    return WorkOrder_df

def transform_avgQty(WorkOrder_df, Product_df):
    ## transforming data
    AVGQty = WorkOrder_df.groupBy("ProductID").mean("OrderQty").withColumnRenamed("AVG(OrderQty)", "AVG_Qty")

    print(AVGQty.show())

    JoinTb_df = Product_df.join(AVGQty, Product_df.ProductID == AVGQty.ProductID).select(AVGQty.ProductID, AVGQty.AVG_Qty, Product_df.Name)
    JoinTb_df.drop("ProductID")

    ##print(JoinTb_df.show())

    return JoinTb_df

## load transformed data to database
def load_df_to_database(JoinTb_df):
    JoinTb_df.write \
        .format("jdbc") \
        .option("url", "jdbc:sqlserver://;serverName=localhost;databaseName=AdventureWorks2022;integratedSecurity=true;encrypt=true;trustServerCertificate=true") \
        .option("dbtable", "AVGQty") \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .save()

if __name__ == "__main__":
    Product_df = extract_Product_to_df()
    WorkOrder_df = extract_WorkOrder_to_df()
    JoinTb_df = transform_avgQty(WorkOrder_df, Product_df)
    load_df_to_database(JoinTb_df)