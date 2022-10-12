
class Client:
    state = "end"
    name=0
    def __init__(self,name):
        self.name = name
        self.proxys = []

    def send(self, msg):
        msg = "client [" + str(self.name) + "] echo > " +msg+" <" 
        print(msg)
    def connect(self, proxy):
        proxy.register(self)
    def recieve(self):
        return self.name