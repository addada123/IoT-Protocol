import random
import time
from kafka import KafkaConsumer
from paho.mqtt import client as mqtt_client
import json

consumer = KafkaConsumer("test")
broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, consumer):
    msg_count = 0
    while True:
        for msg in consumer:
            time.sleep(1)
            message = msg
            result = client.publish(topic, message)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{message}` to topic `{topic}`")
            else:
                print(f"Failed to send message to topic {topic}")
            msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client, consumer)

if __name__ == '__main__':
    run()