import paho.mqtt.client as mqtt
import time
from datetime import datetime
import random

mqttBroker = "192.168.1.102"
client = mqtt.Client("python_test")
client.connect(mqttBroker)

while True:
    date = datetime.now()
    client.publish("test/Sensor1", str(round(random.uniform(20, 30), 1)))
    print("Just published " + date.strftime("%d/%m/%Y %H:%M:%S") + " to Topic test/message")
    time.sleep(60)
