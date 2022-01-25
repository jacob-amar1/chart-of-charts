import kafka
import socket
import os
from datetime import datetime
from time import sleep
from json import dumps
kafka_server = os.getenv("KAFKA_SERVER")
topic = os.getenv("TOPIC")

producer = kafka.KafkaProducer(bootstrap_servers=kafka_server,client_id=socket.gethostname(),
                               value_serializer=lambda x:
                               dumps(x).encode('utf-8'))
while True:
   now = datetime.now()
   current_time = now.strftime("%H:%M:%S")
   message = {"current time is": current_time}
   producer.send(topic=topic,value=message)
   print(message)
   sleep(1)