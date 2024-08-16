#!/usr/bin/env python
import pika
import time 
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

while 1:
    channel.exchange_declare(exchange='direct_msg',
                         exchange_type='direct')
    payload = f"Hello World! {random.randint(0,1000)}"
    channel.basic_publish(exchange='direct_msg', routing_key='provider', body=payload)
    print(f"[x] Sent '{payload}'")
    time.sleep(1)