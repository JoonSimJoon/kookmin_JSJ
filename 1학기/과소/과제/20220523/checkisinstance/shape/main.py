import myshape # myshape.py
listShapes = []
c1 = myshape.Circle(0, 0, 10)
c2 = myshape.Circle(10, 20, 20)
r1 = myshape.Rectangle(10, 20, 30, 40)
r2 = myshape.Rectangle(40, 30, 20, 10)
s1 = myshape.Square(0, 0, 10)
s2 = myshape.Square(10, 20, 30)
listShapes.append(c1)
listShapes.append(c2)
listShapes.append(r1)
listShapes.append(r2)
listShapes.append(s1)
listShapes.append(s2)
for s in listShapes:
    s.draw()
    print(str(s))
print("The number of shapes created: " +
    str(myshape.Shape.numShapes))
print("The number of rectangles created: " +
    str(myshape.Rectangle.numRectangles))
print("The number of squares created: " +
    str(myshape.Square.numSquares))
print("The number of circles created: " +
    str(myshape.Circle.numCircles))