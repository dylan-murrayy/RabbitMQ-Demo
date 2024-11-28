import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')

# Establish a connection and channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Publish a message
message = "Hello, RabbitMQ!"
channel.basic_publish(
    exchange='',
    routing_key=queue_name,
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
)
print(f" [x] Sent: '{message}'")

# Close the connection
connection.close()
