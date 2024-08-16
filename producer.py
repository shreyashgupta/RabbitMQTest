#!/usr/bin/env python
import pika
import time 
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

while 1:
    channel.queue_declare(queue='hello')
    payload = f"Hello World! {random.randint(0,1000)}"
    channel.basic_publish(exchange='', routing_key='hello', body=payload)
    print(f"[x] Sent '{payload}'")
    time.sleep(1)