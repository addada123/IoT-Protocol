# IoT Protocol
 Protocol messaging system with kafka(OPT-UA->MQTT)

Folders explaining;

kafka-spring is an application that I wrote which receives messages with kafka or sends messages with kafka

kafka-js is same application as kafka-spring but in JavaScript

java-opc-ua is a basic java spring messaging server application which uses opc-ua protocol to communicate

python-opc-ua is same as java-opc-ua but in python

In Server-improved
    You should first start docker and write the commands that I've written in kafka-dokcer.txt
    Then start the server_object.py in python-server after that run dummy_client.py -> random_parameter.py
    use kafka-consumer the receive message and you can write a producer to direct message
    
(I've deleted some files to upload that project into github lol. I hope it will still work.)