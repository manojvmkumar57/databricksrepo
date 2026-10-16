from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder.appName("demo").getOrCreate()

df = spark.read.option("header", "true") \
    .csv("gs://banking_bucket2026/raw_data_file/test-data.txt")

filtered_df = df.filter(df["amount"] >= 500)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filtered_df.write.mode("overwrite") \
    .option("header", "true") \
    .csv(f"gs://banking_bucket2026/raw_data_file/customer_{timestamp}")

spark.stop()

print("Cloud Build Test")
