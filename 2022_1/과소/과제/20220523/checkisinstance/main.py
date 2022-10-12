class Parent:
    def __
    pass

class Child(Parent):
    pass

class Sibling(Parent):
    pass

class CChild(Child):
    pass

p = Parent()
c = Child()
s = Sibling()
cc = CChild()


res = isinstance(p, Parent)
print(f"isinstance(p, Parent): {res}")
res = isinstance(c, Child)
print(f"isinstance(c, Child): {res}")
res = isinstance(s, Sibling)
print(f"isinstance(s, Sibling): {res}")
res = isinstance(cc, CChild)
print(f"isinstance(cc, CChild): {res}")
print()
res = isinstance(cc, Parent)
print(f"isinstance(cc, Child): {res}")
res = isinstance(cc, Child)
print(f"isinstance(cc, Child): {res}")
res = isinstance(cc, Sibling)
print(f"isinstance(cc, Sibling): {res}")
print()
res = isinstance(s, Child)
print(f"isinstance(s, Child): {res}")