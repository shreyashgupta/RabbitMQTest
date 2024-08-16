#!/usr/bin/env python
import pika, sys, os
import random


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    num = random.randint(0, 100)
    queue_name = ''
    channel.exchange_declare(exchange="direct_msg", exchange_type="direct")
    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.queue_bind(exchange="direct_msg", queue=queue_name, routing_key="shreyash")

    print("Opened queue: " + queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
