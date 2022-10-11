from square import Square
import math

class InnerCircle(Square):
    def __init__(self, p, q):
        super().__init__(p, q)
    def calculate(self):
        return ((self.p.x-self.q.x)/2)**2*math.pi