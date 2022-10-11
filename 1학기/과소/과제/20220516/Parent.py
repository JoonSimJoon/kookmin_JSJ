class Parent:
    def foo(self):  
        print("Call the function foo of the parent.")
class Pparent:
    def foo(self):  
        print("Call the function foo of the parent.")
class Child(Parent,Pparent):
    def foo(self):
        print("Call the function foo of the child.")
        #super.foo()    
        #Parent.foo(self)
c = Child()
c.foo()
