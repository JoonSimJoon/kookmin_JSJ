class Proxy:
    state = "end"
    name=0
    def __init__(self,name):
        self.name = name
        self.clients =[]
    def start(self):
        self.state="start"
    def __str__(self):
        msg = "Proxy [" + str(self.name) + "] state: " + str(self.state) 
        return msg    
    def register(self, client):
        self.clients.append(client)
    def connect(self, server):
        self.server = server
    def broadcast(self,msg1):
        for c in self.clients:
            port = c.recieve
            msg = "client [" + str(c.name) + "]: broadcast > echo > " +msg1+" <"
            print(msg)  