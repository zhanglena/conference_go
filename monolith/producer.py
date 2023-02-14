import pika  # import the library to connect to RabbitMQ

# Set the hostname that we'll connect to
parameters = pika.ConnectionParameters(host='rabbitmq')

# Create a connection to RabbitMQ
connection = pika.BlockingConnection(parameters)

# Open a channel to RabbitMQ
channel = connection.channel()

# Create a queue if it does not exist
channel.queue_declare(queue='conferences')

# Send the message to the queue
channel.basic_publish(exchange='', routing_key='conferences', body='sending conference')

# Print a status message
print("  Sent 'Hello World!'")

# Close the connection to RabbitMQ
connection.close()
