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
- 
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

        