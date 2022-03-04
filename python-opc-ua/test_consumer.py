from kafka import KafkaConsumer
from opcua.ua.uaprotocol_auto import TransferSubscriptionsParameters

consumer = KafkaConsumer('test', bootstrap_servers = "192.168.1.3:9092")
for msg in consumer:
    print(msg)

