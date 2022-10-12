from square import Square
import math

class OuterCircle(Square):
    def __init__(self, p, q):
        super().__init__(p, q)
    def calculate(self):
        return (math.sqrt((self.p.x-self.q.x)**2 + (self.p.y-self.q.y)**2)/2)**2 *math.pi