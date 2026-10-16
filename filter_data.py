from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder.appName("demo").getOrCreate()

df = spark.read.option("header", "true") \
    .csv("gs://your-bucket/input/customer.csv")

filtered_df = df.filter(df["city"] == "Chennai")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filtered_df.write.mode("overwrite") \
    .option("header", "true") \
    .csv(f"gs://your-bucket/output/customer_{timestamp}")

spark.stop()
