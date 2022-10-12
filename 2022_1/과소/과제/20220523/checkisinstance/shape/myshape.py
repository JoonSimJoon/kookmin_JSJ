import turtle

class Shape:
    numShapes =0

    def __init__(self,x,y) -> None:
        self.x =x
        self.y= y
        Shape.numShapes+=1
    def draw(self):
        turtle.penup()
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.pendown()
    

class Circle(Shape):
    numCircles =0
    def __init__(self,x,y,r) -> None:
        self.x =x
        self.y= y
        self.r =r
        Circle.numCircles+=1
        Shape.numShapes+=1

    def __str__(self):
        return "Circle: Radius=" + str(self.r) + " Shape at (" + str(self.x)+","+str(self.y)+")"
    def draw(self):
        super().draw()
        turtle.circle(self.r)
        turtle.pendown()

class Rectangle(Shape):
    numRectangles =0
    def __init__(self,x,y,h,w) -> None:
        self.x =x
        self.y= y
        self.w = h
        self.h =w
        Rectangle.numRectangles+=1
        Shape.numShapes+=1

    def __str__(self):
        return "Rectangle:  Width=" + str(self.w) +", Height = "+str(self.h)+ " Shape at (" +str( self.x)+","+str( self.y)+")" 
    def draw(self):
        
        turtle.setx(self.x)
        turtle.sety(self.y)
        for i in range(2):
            turtle.forward(self.w)
            turtle.left(90)
            turtle.forward(self.h)
            turtle.left(90)
            
        turtle.pendown()

class Square(Shape):
    numSquares =0 
    def __init__(self,x,y,l) -> None:
        self.x =x
        self.y= y
        self.l = l
        Square.numSquares +=1
        Shape.numShapes+=1
        
    def __str__(self) :
        return "Square : Width=" + str( self.l) +", Height = "+ str( self.l)+ " Shape at (" + str( self.x)+","+ str( self.y) +")" 
    def draw(self):
        
        turtle.setx(self.x)
        turtle.sety(self.y)
        for i in range(2):
            turtle.forward(self.l)
            turtle.left(90)
            turtle.forward(self.l)
            turtle.left(90)