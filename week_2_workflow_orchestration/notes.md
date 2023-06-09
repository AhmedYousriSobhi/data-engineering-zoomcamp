# Data Lake

## Data Swamp
- Data Lake containing unstructed, ungoverned data, that has gotten out of hand.

    For example, Storing data in specific format, then chagning the format and continue storing in same folder location.
        - That makes it hard for consumers to consume it, then the data become useless.

    Result of lack of process and standars.
        - No Versioning.
        - Incompatible shcemas for same data without Versioning.
        - No metadata associated.

    Diffuclt to find, manuipulate, and inevitably-analyze.

## Cloud Providers for Data Lake

- GCP - cloud storage.
- AWS - S3.
- AZURE - AZURE BLOB.

# Data Orchestration
To fully understand how we got to this concept of Orchestration, let's go back a little bit to understand what were there.

## Data Silo
- A collection of data that is isolated from other data within an organization.
- This could happen for a variety of reasons, such as:
    - __Different departments__ using different software systems.
    - Data being stored in __different formats__.
    - Data being stored in __different locations__.
    - Data being __owned by different teams or individuals__.

- Data silos can have a number of __negative consequences__ for an organization, including:
    - __Reduced efficiency__: Data silos can make it difficult to share data between departments, which can lead to duplication of effort and wasted time.
    - __Reduced agility__: Data silos can make it difficult to respond to changes in the market or customer demands.
    - __Reduced innovation__: Data silos can make it difficult to identify new opportunities or develop new products and services.
    - __Increased risk__: Data silos can make it more difficult to comply with regulations and protect data from security breaches.

- There are a number of things that organizations can do to address the problem of data silos, such as:
    - Standardizing data formats and processes
    - Investing in data integration tools
    - Creating a data governance framework
    - Promoting a culture of data sharing

- By taking these steps, organizations can break down data silos and unlock the value of their data.

- Here are some of the challenges of data silos:
    - __Data duplication__: When data is siloed, it is often duplicated across different systems. This can lead to data inconsistencies and errors.
    - __Data fragmentation__: Data silos can lead to data fragmentation, which means that data is stored in different formats and locations. This can make it difficult to access and analyze data.
    - __Data security__: Data silos can make it difficult to protect data from security breaches. This is because data is often stored in different systems and locations, which can make it difficult to track and monitor.
    - __Data governance__: Data silos can make it difficult to implement data governance policies and procedures. This is because data is often owned by different teams or departments, which can lead to conflicting priorities and goals.

- Here are some of the benefits of breaking down data silos:
    - __Improved decision-making__: When data is siloed, it can be difficult to get a complete picture of the business. This can make it difficult to make informed decisions.
    - __Increased efficiency__: When data is siloed, it can be difficult to share data between departments. This can lead to duplication of effort and wasted time.
    Improved customer service: When data is siloed, it can be difficult to provide personalized customer service. This can lead to customer dissatisfaction and churn.
    - __Increased innovation__: When data is siloed, it can be difficult to identify new opportunities or develop new products and services.
    - __Reduced risk__: When data is siloed, it can be more difficult to comply with regulations and protect data from security breaches.

- If you are looking to break down data silos in your organization, there are a number of steps you can take. These include:
    - __Standardizing data formats and processes__: This will make it easier to share data between systems.
    - __Investing in data integration tools__: This will help you to connect different systems and bring data together into a single view.
    - __Creating a data governance framework__: This will help you to define roles and responsibilities for managing data.
    - __Promoting a culture of data sharing__: This will help to break down silos and encourage people to share data.

## Hirtory of word Orchestration
- The word orchestration in data orchestration comes from the classical music definition of orchestration, which is the study or practice of writing music for an orchestra. In data orchestration, the same principles are applied to the automated configuration, coordination, and management of computer systems and software. Just as a conductor leads an orchestra, a data orchestrator leads a team of data engineers and architects in the process of collecting, transforming, and delivering data to users.

- The term data orchestration was first coined in the early 2000s, as businesses began to move away from traditional data warehouses and towards more agile and scalable data architectures. In these new architectures, data is often stored in a variety of different locations, including on-premises, in the cloud, and in third-party data lakes. This can make it difficult to manage and analyze data, which is where data orchestration comes in.

Here are some of the benefits of data orchestration:
- __Improved data quality__: Data orchestration platforms can help to improve data quality by ensuring that data is consistently formatted and validated.
- __Increased data agility__: Data orchestration platforms can help to increase data agility by making it easier to move data between different storage locations and applications.
- __Better decision-making__: Data orchestration platforms can help businesses to make better decisions based on data by providing them with a single view of their data.


## Workflow Orchestration    
- Means govering your data flow in a way that respects orchestration rules and your business logic.

- Orchestration is the coordination and management of multiple computer systems, applications and/or services, stringing together multiple tasks in order to execute a larger workflow or process

- Workflow: a system for managing repetitive processes and tasks which occur in a particular order.

- Workflow orchestration tool is going to allow you to turn any code into a workflow that you can schedule run and observe.

     - Like Apache Airflow, Prefect.

        Apache Airflow:    
        - 2015, by AirBnb
        - Based on core concept of Directed Acyclic Graph (DAG)
                
        ![image](https://cloud.google.com/static/composer/docs/images/workflow-group-dags.png)

        - DAG is a python script, that contains all these controllers functions.
        - Each task is a python script, performs some function on the data, such as cleaning, organizing, ingesting, computing metrics, ... etc.
        
        ![image](https://github.com/AhmedYousriSobhi/DeepLearning.AI-Deep-Learning-Specialization/assets/66730765/eeda5dd6-24a3-46d8-ab55-4c3c4b0d6e6a)

        