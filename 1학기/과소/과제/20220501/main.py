from client.client import Client
from server.server import Server
from proxy.proxy import Proxy

server = Server("My Server")
server.start()
print(server)

proxy = Proxy(1000)
proxy.start()
proxy.connect(server)
print(proxy)


client_01 = Client(1001)
client_02 = Client(1002)
client_03 = Client(1003)
client_04 = Client(1004)
client_05 = Client(1005)

client_01.connect(proxy)
client_02.connect(proxy)
client_03.connect(proxy)
client_04.connect(proxy)
client_05.connect(proxy)

client_01.send("Hello World")
client_02.send("Hello")
client_03.send("Kookim")
client_04.send("Kookim Univ.")
client_05.send("Hello Kookim Univ.")
proxy.broadcast("Hi! there.")
