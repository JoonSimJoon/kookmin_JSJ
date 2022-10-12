
class Server:
    state = "end"
    def __init__(self,name):
        self.name = name
        self.clients = []
    def start(self):
        self.state="start"
    def __str__(self):
        msg = "Server [" + str(self.name) + "] state: " + str(self.state) 
        return msg
    def register(self, client):
        self.clients.append(client)