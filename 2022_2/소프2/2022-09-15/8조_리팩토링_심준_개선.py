score = int (input("enter score: "))
dict = {'10':'A','9':'A','8':'B','7':'C'}

print ("ur score is ", score, ", Grade is ", \
    dict[str(int(score/10))] if 70<=score<=100 else "F")
