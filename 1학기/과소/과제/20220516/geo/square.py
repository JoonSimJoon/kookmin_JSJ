from point import Point

class Square:
    def __init__(self,p,q):
        self.p = p
        self.q = q
    def calculate(self):
        return (self.p.x - self.q.x) * (self.p.y - self.q.y)