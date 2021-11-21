import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

mqttBroker = "192.168.1.102"
client = mqtt.Client("python_test2")
client.connect(mqttBroker)

while True:
    date = datetime.now()
    client.publish("test/Sensor2", str(round(random.uniform(20, 30), 1)))
    print("Just published " + date.strftime("%d/%m/%Y %H:%M:%S") + " to Topic test/message")
    time.sleep(60)
