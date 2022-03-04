from opcua import Server
from random import randint
import datetime
import time as Time

server = Server()
url = "opc.tcp://192.168.1.3:8080"
server.set_endpoint(url)

name = "Demo"

addspace = server.register_namespace(name)

node = server.get_objects_node()

param = node.add_object(addspace, "Parameters")

temp = param.add_variable(addspace, "temp", 0)
parameter = param.add_variable(addspace, "parameter", 0)
ttime = param.add_variable(addspace, "Time", 0)




temp.set_writable()
parameter.set_writable()
ttime.set_writable()



server.start()
print(f"Server has started at {format(url)}")
try:
    while True:

        temperature = randint(10, 50)
        parameter2 = randint(10, 50)

        TIME = datetime.datetime.now()

        print(temperature)
        temp.set_value(temperature)

        print(parameter2)
        parameter.set_value(parameter2)

        print(TIME)
        ttime.set_value(TIME)


        Time.sleep(2)
    
except:
    server.stop()