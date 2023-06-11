# Data Warehouse & Big Query
## OLAP vs OLTP
- OLTP "Online Transaction Processing"
- OLAP "Online Analytical Processing"

![OLAP vs OLTP](https://github.com/AhmedYousriSobhi/DeepLearning.AI-TensorFlow-Developer-Specialization/assets/66730765/864bcce8-18e2-410e-8fe9-69792e543e2d)
![OLAP vs OLTP 2](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/cb81b358-fccf-4b2f-be7a-b57e2e2477d7)

## Data Warehouse
It is a OLAP Solution, Used for reporting and data analysis

![Data warehouse diagram](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/87130b41-90fe-43e9-aaf9-a8f73a25c30b)

From the diagram, there are inputs and outputs to data warehouse.
- Data warehouse consists of: Meta data, Raw data, and Summary data.
- Inputs: differents data sources, could be also from OLTP database source.
- Outputs: Data transfromed into Data marts, which could be purchasing, sales, or inventory data.
    - For Analysis, It could be better to have data into data marts.
    - For data scientist, It could be better to deal with data in its Raw format.
    - So data warehouse support all these possiblities in data.

## BigQuery
It is Data warehouse solution, but thery are __serverless data warehouse__, There are no servers to manage or database software to install.

Usually, for starter companies, they spend alot of time creating the data warehouse, trying to mentain it, So all of these are being elevated by using BigQuery.

BigQuery provides software as well as infrastructure, including scalability and high-availability.

Built-in features like:
- Machine Learning.
- Geospatial Analysis.
- Business Intelligence.

Big Query Maximizes the flexibility of how it store the data.
- Ususally, you have one big server storage and compute togther, but once you data size increases, so your machine should grow with it.
- So bigquery take advantages by seperating the compute engine that analyzes your data from your storage.

### Partioning in BQ
Partioning a table only divides it into "chunks" based on the partion function.

Sectioning data by specific range or interval so the query doesn't have to read the entire table. 
- This enhance the query performance.
- Also Bigquery pricing is based on the amount of data processed in a query, so we limit the amount of data processed using a partionined table, so this will reduce the cost.
![Partion](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/ce961551-8a84-42d3-bd66-3da22699613c)

Partioning provides granular query cost estimates before you run a query.

#### KeyFeatures
- Time-unit Column.
- Ingestion time (_PARTIONTIME)
- Integer range partioning.
- When using time unit or ingestion time
    - Daily (default).
    - Hourly.
    - Monthly or yearly.
- Number of partions limit is 4000.
    - Resource from cloud.google.com/bigquery/docs/partitioned-tables

### Clustering in BQ
Clustering index will give order to the data within each partion.
![Clustering](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/01a1f861-1068-4527-b0f9-47432d3b8eef)
Here we partioned by Data, like we did in Partioning, but also we clustered using the tags.

This helps us to improve our cost, as well as improve our query performance.

When you cluster a table, you're basically choosing how to physically sort it while stored.

Note, Clustering is only supported for partitioned tables.

#### Key Features
- Column you specify are used to colocate related data.
- Order of the column is important.
- The order of the specified columns determines the sort order of the data.
    - ex, you have columns {A, B, C, D}, so clustering will be based on the columns orders you speficy, A, B, C, Then D.
- Clustering impproves
    - Filter queries.
    - Aggregate queries.
- Table with data size < 1GB, don't show significant improvement with partioning and clustering.
- You can specify up to foud clustering columns.
- Clustering columns must be top-level, non-repeqted columns.
    - {DATE, BOOL, GEOGRAPHY, INT64, NUMERIC, BIGNUMERIC, STRING, TIMESTAMP, DATETIME}.

### Comparison between Partioning & Clustering
![Partion vs Cluster](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/fdd1726b-1447-4f7c-afbc-6088c4e45a1d)

### Clustering over partioning
Partitioning results in  a small amount of data per partion (approximately less than 1 GB).

Partitioning results in a large number of partions beyond the limits on partitioned tables.

Partitioning results in your mutation operation modifying the majority of partitions in the table frequently (for example, every few minuites).

### Automatic Reculstring
As data is added to a clustered table
- The newly inserted data can be written to blocks that contain key ranges that overlap with the key ranges in previously written blocks.
- These overlappong keys weaken the sort property of the table.

To maintain the performance characteristics of a clusterd table
- BigQuery performs automatic re-clustering in the background to restore the sort property of the table.
- For partitioned tables, clustering is maintained for data within the scope of each partition.

### BigQuery-Best Practice
#### Cost Reduction
- Acoid SELECT * , * results in reading all the columns, so it is good practice to see the price of the query before you run it, and to specify the columns you want to select.
- Price your queries before running them.
- Use clustered or partitioned tables.
- Use streaming inserts with cautio, they could actually increas the cost.
- Materialize query results in stages.

#### Query Performance
- Filter on partitioned columns.
- Denormalizing data.
- Use nested of repeated columns.
- Use external data sources approprately.
- Don't use it, in case you want a high query performance.
- Reduce data before using a JOIN.
- Do not treat WITH clauses as prepared statements.
- Avoid overshading tables.
- Avoid JavaScript user-defined functions.
- Use approximate aggregation functions (HyperLogLog++).
- Order Last, for query operations to maximize performace.
- Optimize your join patterns.
As a best practice, place the table with the largest number of rows first, followed by the table with the fewest rows, and then place the remaining tables by decreasing size.

### Internals of BigQuery
![Internals of BQ](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/79796d0f-7ef9-44a8-a7db-38653bb6b178)

1- BigQuery stores the data into a seperate storage called __Colossus__, which is a cheap storage, store the data in a column format.
![Column vs row based](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/b7461c4e-15af-484c-90a1-bc21fe4f5423)
- This come with advantage, as BQ has seperated storage from COMPUTE, which lead to significally less cost.
- So if you data increased, so you will only have to pay for data storage in Colssus which is very cheap.

Most of the payment, is during running the query, which is basically is COMPUTE.

2- Question: How Starge and COMPUTE communicate with each other?
- If internet connection between them is very bad, that leads to high running time for query --> Disadvantage.
- __Jupiter__, Come here to resuce us!!, they are inside BQ data centers, provides up to 1TB network speed.

3- __Dremel__ is the COMPUTE engine
- Divide your query into tree structure.
- Seperate your query in such a way, that each node can excute as individual subset of the query.

![Dremel](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/8c9a7288-a473-4b16-bf1e-5a928504125f)
