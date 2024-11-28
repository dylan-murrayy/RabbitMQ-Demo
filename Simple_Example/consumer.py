import pika

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')

# Establish a connection and channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the same queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Define a callback function to handle messages
def callback(ch, method, properties, body):
    print(f" [x] Received: {body.decode()}")

# Start consuming messages
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()

