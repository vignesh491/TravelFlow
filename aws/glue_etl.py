from pyspark.sql import SparkSession
from pyspark.sql.functions import year, month

spark = SparkSession.builder.appName("TravelFlowETL").getOrCreate()

customers = spark.read.option("header", True).csv(
    "s3://travelflow-data/raw/customers.csv"
)

bookings = spark.read.option("header", True).csv(
    "s3://travelflow-data/raw/bookings.csv"
)

destinations = spark.read.option("header", True).csv(
    "s3://travelflow-data/raw/destinations.csv"
)

result = (
    bookings
    .join(customers, "customer_id", "left")
    .join(destinations, "destination", "left")
)

result = result.withColumn(
    "booking_year",
    year("booking_date")
).withColumn(
    "booking_month",
    month("booking_date")
)

result.write.mode("overwrite").parquet(
    "s3://travelflow-data/processed/"
)

result.filter(
    result.status == "confirmed"
).write.mode("overwrite").parquet(
    "s3://travelflow-data/curated/"
)

spark.stop()