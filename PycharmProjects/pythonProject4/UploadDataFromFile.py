import pyspark

# file location and type
file_location = "/Temp/test.csv"
file_type = "csv"

# CSV options
infer_schema = "False"
first_row_is_a_header = "True"
delimiter = ","

# creating dataframe for CSV file
df = spark.read.format
