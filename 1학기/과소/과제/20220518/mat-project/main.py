from mat2d import Mat2D

m1 = Mat2D([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Mat2D([[1], [0], [0]])
print("m1 + m1 = ")
ret = m1 + m1
print(ret)
print("m1 - m1 = ")
ret = m1 - m1
print(ret)
print("m1 * m1 = ")
ret = m1 * m1
print(ret)
print("m2 + m2 = ")
ret = m2 + m2
print(ret)
print("m2 - m2 = ")
ret = m2 - m2
print(ret)
