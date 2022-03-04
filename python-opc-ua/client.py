from opcua import Client
import json
import time
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers = '192.168.1.3:9092')
url = "opc.tcp://192.168.1.3:8080"
client = Client(url)
client.connect()
print("Client connected")


while True:
        temp = client.get_node("ns=2; i=2")
        Temperature = temp.get_value()
        paramtere = client.get_node("ns=2; i=3")
        Parameter = paramtere.get_value()
        Time = client.get_node("ns=2; i=4")
        TIME = Time.get_value()

        print(Temperature)
        print(Parameter)
        print(TIME)
        data = {"Temperature" : f"{Temperature}", "Parameter" : f"{Parameter}", "Time" : f"{TIME}"}
        json_data = json.dumps(data)
        print(json_data)
        producer.send('datas', json_data.encode("utf-8"))
        time.sleep(2)

