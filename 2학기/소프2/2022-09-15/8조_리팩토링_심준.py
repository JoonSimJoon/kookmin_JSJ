score = int (input("enter score: "))

print ("ur score is ", score, ", Grade is ", \
    chr((int((100-score)/10))+65) if 70<=score<=100 else "F")
