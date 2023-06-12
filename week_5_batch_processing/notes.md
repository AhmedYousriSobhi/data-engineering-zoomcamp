# Batch Processing
## Different types of processing data


![Batch1](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/da65485a-f5a4-4d88-bba9-c418bca4d92b)

Orchestration Tool
![workflow](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/12381f7f-2eb6-4122-a689-9b52723e28c5)

This is the main disadvantage of batch processing, it takes some time to process before we could use the data we collected.
- ex, let's assume each step in the workflow, takes around 5 minute to run, and we collect data every 1 hour, so we will have to wait for ~90 mins, before we can use that data.
- This could be solved usign streaming, in the next week.
![image](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/311b35f4-8c0e-4bbd-868b-5a1389c99f96)

## Advantages of Batch
- Easy to manage.
- Retry.
- Scale.

## Disavantage
- Delay.

# Spark
Data processing Engine.

It's distributed, so there is a cluster, which contains tons of machines which pull the input data, then save it somewhere.

Multi-language engine, we could use {JAVA, SCALA, Python, R}.
- Python is quite popular, so they usually use pyspark.

## When yo use Spark
![image](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/fbd8288f-4927-423b-ac78-8b9c679e2f06)
Datalake, located in S3/GCS.

Spark will pull these data to do some processing, then pull it back to Datalake

Using {HIVE, Presto, Athena} to excute SQL on your data in DL, then back them into DL aswell.
- Note, If you can express your batch job as SQL, then go with them. As sometimes, it becomes difficult to use them, So in this case we use SPARK.
- Like in Case of workflow in Machine learning, Usually SPARK is used in that case.

![image](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/71ac4068-4e2d-40f0-9341-45ee4a9172cc)
Raw Data -> Put in DL -> Doing some processing/joining using SQL ATHENA (for ex) -> Doing some complex transformation which we can not do using SQL, So we use SPARK -> Python script job for creating a training ML model -> Then we may have another flow for using the ML model, so we have another SPARK job for taking this model, to apply that model -> ingest the results back to DL.

## SPARK Internals - Partition
![Internals_!](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/a1209456-da65-45dd-b900-070692712853)
### Case of Data are splitted into buckets
Let's assume we have our data buckets in GCS 'Google Cloud Storage', and our data are splitted into buckets.

Spark cluster is splitted into several excuters "Machine".

So each bucket will be assigned to seperate excuter.

So when an excuter finish processing a file bucket, then it will move to the next unprocessed file bucket and start processing it.
- Grayed files are the processed ones so far.

### Case only one Data file
![image](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/0401cd61-bb1e-4c25-ab7b-e3f766e748f3)
Only one excuter will pick this file, and start processing it. The rest of excuters will be idles.

### Summary
In pyspark this is called Partitions, Splitting into multiple partitions is better than only one partition.

Code
```
df = df.repartition(n)
```
This will partition dataframe into n partitions.

It is a lazy command, it does not trigger the partitioning yet, but it will be applied when we do some process on it like saving it.
```
df.write.parquet('filelocation')
# df.write.parquet('filelcoation', mode='overwrite') # incase we want to overwrite the partition files.
```
You can visualize what is happening, the working jobs, each stage, from the localhost/4004 of spark.

This partioning command will be taking too long, because it will a heavy excustion command.

## SPARK Dataframes
Things that are not excuted right aways, are called __Transformations__, which are lazy and not excuted immediatly.
- Selecting columns.
- Filtering columns.
- Applying some functions on columns.
- joins, groupby

Until we do an __Action__, Then SPARK will excute all these stages requested, These actions are called eager and excuted immediately.
- show, take, head, write

![Spark](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/d98d29d5-6b3c-4a21-a7df-65414cd714d2)

### SPARK available defined functions
```
from pyspark.sql import functions as F
# Create a new column
df \
    .withColumn('pickup_date', F.to_date(df.pickup_datetime)) \
    .select('pickup_date', 'another column') \
    .show()
```
### SPARK user defined functions
SPARK support user-defined functions.

```
def crazy_stuff(base_num):
    # return number in hex format
    num = int(base_num[1:])
    if num%7 == 0:
        return f's/{num:03x}'
    else:
        return f'e/{num:03x}'

# Convert this into user defined function
crazy_stuff_udf = F.udf(crazy_stuff, returnType=types.StringType()) 

df \
    .withColumn('pickup_date', F.to_date(df.pickup_datetime)) \
    .withColumn('base_id', crazy_stuff_udf(df.dispatching_base_num)) \
    .select('base_id', 'pickup_date', 'another column') \
    .show()
```

### SQL in Dataframe
To register dataframe as table to use SQL
```
df.registerTemplate('trips_data')

spark.sql("""
SELECT
    COUNT(1)
FROM trips_data LIMIT 10;
"""
)
```