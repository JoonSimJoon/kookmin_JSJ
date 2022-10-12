score = int (input("enter score"))

if 90 <= score <= 100:
    print ("ur score is ", score, ", Grade is A")
elif 80 <= score < 90:
    print ("ur score is ", score, ", Grade is B")
elif 70 <= score < 80:
    print ("ur score is ", score, ", Grade is C")
else:
    print ("ur score is ", score, ", Grade is F")