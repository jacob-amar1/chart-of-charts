from kafka import KafkaConsumer
from time import sleep
import os
import socket

kafka_server = os.getenv("KAFKA_SERVER")
topic = os.getenv("TOPIC")
consumer = KafkaConsumer(
        topic,
        bootstrap_servers=[kafka_server],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=socket.gethostname(),
        )
while True:
  for message in consumer:
          print(message.value)
          sleep(1)