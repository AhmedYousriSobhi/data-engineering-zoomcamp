# Introduction to Analytics Engineering
## Analytic Engineering
![Comparison](https://www.getdbt.com/ui/img/guides/analytics-engineering/analytics-engineer-role.png)

__Data Engineer__ does not included in business and decision making in a company.
- Someone who builds the infrastructure to support the storing and movement of data.
- They are not looking at the data itself, but rather focusing on how they can support the data.
- Includes using python to write data pipeline, spark to process data, and cloud technologies like AWS to deploy infrastructure.
- Data Engineer work closely with other developers such as software engineers.
- The day-to-day of a data engineer involves meeting with a scrum master to help prioritize your tasks and move you along.
- Top skills: {Python, AWS, Git, Bash, Spark, Hadoop}

__Analytical engineering__ role includes both technical and business exposure. Require collaboration across different teams within a company.
- Someone who moves and transforms data from the source so that it can be easily analyzed, visualized, and acted upon by the data analyst or business user.
- Deal with data itself as well as the moving of data.
- Their job to make sure data is ingested, transformed, shceduled, and ready to be used for analytics.
- Many Analytics engineers are the brains behind the "model data stack".
- Decide which tool to use for ETL/ELT.
- Top skills: {SQL, Experience with DBT, Communication, Python, Experience with modern data stack tools (snowflake, google big query, fivetran, matillion, Airbyte, Looker, Thoughtspot)}

![Tooling](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/6b45ae62-d7ad-4a2f-bcfe-e62b7f303a49)

### What analytics engineering is not
- Not building the architecture to support the data.
- Not your typical software development language.
- Not only interacting with other engineers and product owners.

Research [source](https://www.thoughtspot.com/data-trends/data-and-analytics-engineering/analytics-engineer-vs-data-engineer)

## ELT vs ETL
![ETL vs ELT](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/466b8e39-96c9-49f0-9efc-ce5dc15c85d2)
ETL: Export, Transform, Load
- Small amount of Data.
- __Schema on write__, means define schema, define relationships, then write the data.
- Ex, Data Warehouse -> Structured data. which is required for business need.

ELT: Export, Load, Transform
- Large amount of Data.
- __Schema on Read__, means Write the data, then define the schema, define the relationships.
- Ex, Data Lake -> Unstructured data, Reason for it, consumers are in a hurry for the data, so there were not much time for transformation.
 
## Data Modeling
It is the process of analyzing and defining all the different data your business collects and produces, as well as the relationships between those bits of data.

### Types of Data Modeling
Research [Source](https://www.couchbase.com/blog/conceptual-physical-logical-data-models/)

#### __Coceptual data models__

![Conceptional data model](https://www.couchbase.com/blog/wp-content/uploads/2022/10/image1-1.png)

- Can be thought of as the "white board" data model, this model does not go into the 'how' at all.
- In this model, it is important to focus on capturing all the types of data (or entities) that the system will need.
- The entities which the conceptional model will capture:
    - Attributes: individual properties of an entity. For instance, a “person” entity may have “name” and “shoe size”. An “address” entity may have “zip code” and “city”.
    - Relationships: how an entity connects to other entities, for instance, a 'person' entity may have one or more 'addresses'.
- Along with entities, a conceptual model can also:
    - Organize scope: which entities are included, but also which are explicitly NOT included.
    - Define business concepts/rules: For instance, are person entities allowed to have multiple addresses? What about multiple emails? Do they need to have a unique identifier?.
- While this may look like tables in a relational database, the conceptual modeling stage is too early to make a determination about how the data will be stored. This determination comes later: it could be tables, JSON documents, graph nodes, CSV files, blockchain, or any other number of storage mediums.

#### __Logical data models__
- Logical data model is the next step, once the stakeholders have agreed on a conceptual model.
- This step involces filling the details of the conceptual model.
- It is still too early to pick a specific DBMS, but this step can help you decide which class of database to use (relational, documents, etc).
- For instance, if you decide relational, then it's time to decide which tables to create. if you decide document, then it's time to define the collections.
- Relational model, the logical model might look like this
    - ![Logical data model](https://www.couchbase.com/blog/wp-content/uploads/2022/10/image3.png)
- Document database, the schedule can be modeled as part of the route, directly. No need for a foreign key, but it’s still helpful to think of it as its own sub-entity. So that logical model might look like this:
    - ![Document logical model](https://www.couchbase.com/blog/wp-content/uploads/2022/10/image2-1.png)

Physical data models
- Once the logical mode has been defined, it's now time to actually implement it into a real database.
- If you decide a relational model, options include SQL server, Oracle, PostgresSQL, MySQL, etc.
- However, if you modeling process reveals that your data model is likely to change frequently to adapt to new requirments, you might still consider going with a document database.
- One of the best choices for this is Couchbase, a “NoSQL” document database that supports familiar relational concepts like JOINs, ACID transactions and flexible JSON data.
- The physical data model should include:
    - A specific DBMS (Couchbase, for instance).
    - How data is stored (on disk/RAM/Hybrid)/
    - How to accommodate replication, shards, partitions.
- Physical data model is typically creted by DBAs and/or developers.
- ![Physical Data model](https://www.couchbase.com/blog/wp-content/uploads/2022/10/image4.png)

#### Comparison
Each model is a necessary step on a journey to build a useful data model for you applications. A conceptual data model is the highest level, and therefore the least detailed. A logical data model involves more detailed thinking about the implementation without actually implementing anything. Finally, the physical data model draws on the requirements from the logical data model to create a real database.

### Advantages of Data Modeling
Short term communication among stakeholders to make decision about what's important, what the business rules are, and how to implement them.

Long term communication through database specification that can be used to connect your data to other services through ETLs.

### Disadvantages of Data Modeling
It can be potentially long process. t can also be prone to waterfall mentality (e.g. a mistake found during the logical data modeling process could trigger a complete rework of the conceptual modeling process).

A physical relational model can be rigid and difficult to change once a physical data model has been created (especially in production).

A physical document model is easy to change at any time, but relies on the application layer to enforce constraints and data types.

### Kimball's Dimentional Modeling
Objective
- Deliver data understanable to the business users.
- Deliver fast query performance.

Approach
- Prioritise user understandability and query performance over non redundant data (3NF)

Other approaches
- Bill Inmon.
- Data Vault.

### Elements of Dimensional Modeling
Also known as __Star schema__
![Star Schema](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/5481a14c-ba0a-4396-b4f5-987cac1352d5)

Fact Tables
- Measurements, metrics or facts.
- Coreesponds to a business process.
- Think about them like 'verbs', like Sales

Dimensions Tables
- Corresponds to a business entity.
- Provides context to a business process
- Think about them like 'Nouns' like customers, or products

### Architecture of Dimensional Modeling
![Restaurant](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/7c404597-290b-47be-a155-252fbfe70385)

Stage Area "Market"
- Contains the raw data.
- Not meant to be exposed to everyone, only who are able to use raw data and make use out of it.

Processing Area "Kitchen"
- From raw data to data models.
- Focuses in efficiency.
- Ensuring Standards.

Presentation Area "Dining Hall"
- Final presentation of the data.
Exposure to business stackholder.

## Star Schema vs Snowflake Schema
![start vs snowflake](https://cdn.buttercms.com/JkKvqxXHSRSFqZed2mDg)


# dbt
Stands for Data Build Tool, that build on SQL

According to dbt, the tool is a development framework that combines modular SQL with software engineering best practices to make data transformation reliable, fast, and fun.

dbt is a transformation tool that allows anyone that knows SQL to deploy analytics code following software engineering best practices
- Like modularity, portability, CI/CD "continuous integration and continuous delivery/continuous deployment", and Documentation.

![dbt](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/07be048e-fda9-4302-87c8-0bb72aaaab0e)

![dbt](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/b8651a93-518d-40c7-abbd-20c25c54b586)

So DBT turned SQL from it is analytic like thing, to more code-like/engineered like.

dbt (data build tool) makes data engineering activities accessible to people with data analyst skills to transform the data in the warehouse using simple select statements, effectively creating your entire transformation process with code. 

You can write custom business logic using SQL, automate data quality testing, deploy the code, and deliver trusted data with data documentation side-by-side with the code. 

This is more important today than ever due to the shortage of data engineering professionals in the marketplace. Anyone who knows SQL can now build production-grade data pipelines, reducing the barrier to entry that previously limited staffing capabilities for legacy technologies.

In short, dbt (data build tool) turns your data analysts into engineers and allows them to own the entire analytics engineering workflow.

Prerequisites to Getting started with dbt
- {SQL, Modeling, Git}

For more [info](https://www.analytics8.com/blog/dbt-overview-what-is-dbt-and-what-can-it-do-for-my-data-pipeline/#).

## How does it work
![dbt work](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/7051698a-6a4b-4c78-9190-07d2e61a1dce)

- Starting from "pink cylinder" our data warehouse where we have our raw data.
- Creating a modeling layer, where we will transform our data.
- Then this model, with the transformed data, will persist back to the data warehouse.

How this is happening !
- First will we write a SQL file, which will be our dbt model.
- It will be basiclly a Select statemetns, but we will not add any DDL or DML.
    - DDL: Data Definition Language, which is used to define data structures, for example: crete table, alter table, instructions in SQL.
    - DML: Data Manipulation Language, which is used to manipulate data itself, for example: insert, update, delete are instructions in SQL.
- Then DBT will compile that file.

So the results we will see in the data warehouse.

## How are we going to use dbt !
BigQuery
- Development using cloud IDE.
- No local installation of dbt core.

Postgres
- Development using a local IDE of you choise.
- Local installation of dbt core connecting to the Postgress database.
- Running dbt model through the CLI.

![How are we goint to use dbt](https://github.com/AhmedYousriSobhi/ATmega-16-BOOTLOADER/assets/66730765/660f5435-b6bb-4bbf-8f4d-53e733b9dc9a)

