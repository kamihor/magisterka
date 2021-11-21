import paho.mqtt.client as mqtt
from db_controller import Database

MQTT_BROKER = "192.168.1.102"
MQTT_SUB_NAME = "spy"


def on_message(client, userdata, message):
    try:
        print(str(message.payload.decode("utf-8")) + " " + message.topic)
        home_db.insert_meas(str(message.payload.decode("utf-8")), home_db.select_id(message.topic)[0])
    except:
        print("no message")


def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + mqtt.connack_string(rc))


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


client = mqtt.Client(MQTT_SUB_NAME)
client.connect(MQTT_BROKER)

home_db = Database("localhost", "root", "", "mqtt_home_db")

client.subscribe("#")
client.loop_start()

while True:
    client.on_message = on_message
