# RabbitMQ Demo

RabbitMQ is a message broker. It helps applications communicate by sending messages to a queue where they can be consumed later. It implements the AMQP 0.9.1 protocol, which defines how messages are formatted, sent, and received between producers and consumers.


### Message Brokers 

RabbitMQ acts as a middleman that receives messages from a producer and stores them in a queue until a consumer retrieves them.

A queue is a data structure inside RabbitMQ where messages are stored Messages stay in the queue until a consumer retrieves them or they expire.
 
Queues can be:
- Durable: Persist on disk, surviving broker restarts.
- Transient: Exist in memory only.

### Producers and Consumers

A producer is an application that sends messages to RabbitMQ. publisher.py is the producer. Producers use channels to communicate with RabbitMQ and send messages to a specific queue.

A consumer is an application that retrieves messages from RabbitMQ. Consumers subscribe to queues, receive messages, and process them (e.g., display, store, or forward).

### Connection and Channel

A connection is a TCP connection between your application and the RabbitMQ broker.

A channel is a virtual connection within a connection. Multiple channels can be used over a single TCP connection.

Channels are lightweight and are used to perform messaging operations like declaring a queue or sending/receiving messages.

### Exchanges and Bindings

An exchange is a routing mechanism that decides how messages are distributed to queues.
Types of exchanges:
- Direct: Routes messages to a queue with a specific routing key.
- Fanout: Broadcasts messages to all queues bound to the exchange.
- Topic: Routes messages based on wildcard routing keys.
- Headers: Routes based on message headers (less common).

A binding connects an exchange to a queue.
It specifies which messages (based on routing keys) should go to which queue.

### Messages 

A message is a payload (data) sent by a producer to a queue.

Messages can have properties, like:
- Delivery mode: Persistent or transient.
- Headers: Metadata for message processing.

### Acknowledgements

When a consumer receives a message, RabbitMQ waits for an acknowledgment (ACK) to confirm the message was processed. 
- Manual ACK: The consumer explicitly sends an acknowledgment.
- Auto ACK: The message is acknowledged as soon as it’s delivered.

