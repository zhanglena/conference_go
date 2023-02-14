import json
import pika
import django
import os
import sys
from django.core.mail import send_mail
import time
from pika.exceptions import AMQPConnectionError


sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "presentation_mailer.settings")
django.setup()

def process_approval(ch, method, properties, body):
    print("  Received %r" % body)
    info = json.loads(body)
    send_mail(
        'Presentation Approved',
        'Your presentation has been approved!',
        "presentation@conferencego.com",
        [info["presenter_email"]],
        fail_silently=False,
)

while True:
    try:# parameters = pika.ConnectionParameters("rabbitmq")
        connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
        channel = connection.channel()
        channel.queue_declare(queue='presentation_approvals')
        channel.basic_consume(
            queue='presentation_approvals',
            on_message_callback=process_approval,
            auto_ack=True,
        )
        channel.start_consuming()
    except AMQPConnectionError:
        print("couldn't connect")
        time.sleep(5)
