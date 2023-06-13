# Steam Processing

## Steaming Data
Streaming data is the continouse flow of information from disparate sources to a destination for real-time processing and analytics.

Example, Credit card companies can use steaming transaction data to detect irregularities and stop fraud before it happenns.

Example, Application can present recommendation to a customer based on their real-time choices leading to better customer experience (Netflix, amazon, Youtube).

Benefit of steaming data, To put it simply, the real-time nature of stream data processing allows data teams to deliver continous insights to business users across the organization.

## Stream Processing vs Batch Processing
In batch processing, data sets are extracted from sources, processed or transformed to make them useful, and loaded into a destination system. ETL processing creates snapshots of the business in time, stored in data warehouses or data marts for reporting and analytics. Batch processing works for reporting and applications that can tolerate latency of hours or even days before data becomes available downstream. 

With the demand for more timely information, batches grew smaller and smaller until a batch became a single event and stream processing emerged. Without a beginning or an end, sliding window processing developed so you could run analytics on any time interval across the stream

## Apache Kafka
### Intro
Research [source](https://www.tutorialspoint.com/apache_kafka/apache_kafka_introduction.htm)

In Big Data, an enormous volume of data is used. Regarding data, we have two main challenges.The first challenge is how to collect large volume of data and the second challenge is to analyze the collected data. To overcome those challenges, you must need a messaging system.

A Messaging System is responsible for transferring data from one application to another, so the applications can focus on data, but not worry about how to share it. Distributed messaging is based on the concept of reliable message queuing. Messages are queued asynchronously between client applications and messaging system. Two types of messaging patterns are available − one is point to point and the other is publish-subscribe (pub-sub) messaging system. Most of the messaging patterns follow pub-sub.

In a point-to-point system, messages are persisted in a queue. One or more consumers can consume the messages in the queue, but a particular message can be consumed by a maximum of one consumer only. Once a consumer reads a message in the queue, it disappears from that queue. The typical example of this system is an Order Processing System, where each order will be processed by one Order Processor, but Multiple Order Processors can work as well at the same time. The following diagram depicts the structure.
![point to point](https://www.tutorialspoint.com/apache_kafka/images/point_to_point_messaging_system.jpg)

In the publish-subscribe system, messages are persisted in a topic. Unlike point-to-point system, consumers can subscribe to one or more topic and consume all the messages in that topic. In the Publish-Subscribe system, message producers are called publishers and message consumers are called subscribers. A real-life example is Dish TV, which publishes different channels like sports, movies, music, etc., and anyone can subscribe to their own set of channels and get them whenever their subscribed channels are available
![pub\sub](https://www.tutorialspoint.com/apache_kafka/images/publish_subscribe_messaging_system.jpg)

### Apache Kafka
It is an open source distributed event streaming platform, known as a __'pub/sub'__ messaging system.

A streaming data source starts publishing or streaming data, and a destination system subscribes to receive the data.

The publisher doesn't wait for subscribers, and subscribers jump into the stream when they need it.

Kafka is fast, scalable, durable, and was a pillar of on-premises big data deployment.

#### Terminologies
![terminologies](https://www.tutorialspoint.com/apache_kafka/images/fundamentals.jpg)
Some terminologies are required to be known: {Topics, brokers, producers, consumers}

__Topic__ 
- A stream of messages belonging to a particular category is called a topic. Data is stored in topics.
- Topics are split into partitions. For each topic, Kafka keeps a mini-mum of one partition. Each such partition contains messages in an immutable ordered sequence. A partition is implemented as a set of segment files of equal sizes.

__Partition__
- Topics may have many partitions, so it can handle an arbitary amound of data.

__Partition offset__
- Each partitioned message has a unique sequence id called as 'offset'.

__Replicas of partition__
- Replicas are nothing but 'backups' of a partition. Replicas are never read or write data. They are used to prevent data loss.

__Brokers__
- Brokers are simple system resposible for maintaining the pub-lished data. Each broker may have zero or more partition per topic. Assume, if there are N partition in a topic and N number of brokers, each broker will be one partition.
- Assume if there are N partitions in a topic and more than N brokers (n+m), the first N broker will have one partition, and the next M brokers will not have any partition for that particular topic.
- Assume if there are N partitions in a topic, and less than N brokers (N-M), each broker will have one or more partition sharing among them. This scenario is not recommended due to unequal load distribution among the broker.

__Kafka Cluster__
- Kafka's having more thatn one broker, are called as Kafka Cluster. A kafka cluster can be expaned without downtime. These clusters are used to manage the persistence and replication of message data.

__Producers__
- Producers are the publisher of messages to one or more Kafka topics. Producers send data to Kafka brokers. Every time a producer publishers a message to a broker, the broker simply append the message to the last segment file. Actually, the message will be appended to a partition. Producer can also send messages to a partition of their choice.

__Consumers__
- Consumers read data from brokers. Consumers subscribes to one or more topics and consume published message by pulling data from the brokers.

__Leader__
- Leader is the node responsible for all reads and writes for the given partition. Every partition has one server acting as a leader.

__Follower__
- Node which follows leader instructions are called as follower. If the leader fails, one of the follower will automatically become the new leader. A follower acts as normal consumer, pulls messages and up-dates its own data store.

#### Cluster Architecture
![cluster](https://www.tutorialspoint.com/apache_kafka/images/cluster_architecture.jpg)
__Broker__
- Kafka cluster typically consists of multiple brokers to maintain load balance. Kafka brokers are stateless, so they use ZooKeeper for maintaining their cluster state. One Kafka broker instance can handle hundreds of thousands of reads and writes per second and each bro-ker can handle TB of messages without performance impact. Kafka broker leader election can be done by ZooKeeper.

__ZooKepper__
- ZooKeeper is used for managing and coordinating Kafka broker. ZooKeeper service is mainly used to notify producer and consumer about the presence of any new broker in the Kafka system or failure of the broker in the Kafka system. As per the notification received by the Zookeeper regarding presence or failure of the broker then pro-ducer and consumer takes decision and starts coordinating their task with some other broker.

__Producers__
- Producers push data to brokers. When the new broker is started, all the producers search it and automatically sends a message to that new broker. Kafka producer doesn’t wait for acknowledgements from the broker and sends messages as fast as the broker can handle.

__Consumers__
- Since Kafka brokers are stateless, which means that the consumer has to maintain how many messages have been consumed by using partition offset. If the consumer acknowledges a particular message offset, it implies that the consumer has consumed all prior messages. The consumer issues an asynchronous pull request to the broker to have a buffer of bytes ready to consume. The consumers can rewind or skip to any point in a partition simply by supplying an offset value. Consumer offset value is notified by ZooKeeper.