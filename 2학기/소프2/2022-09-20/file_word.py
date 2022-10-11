wordcount=dict()

fH=open('test3_1.dat', 'r')
lines =fH.readlines()
fH.close()
for line in lines:
    words = line.split()
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    


for word in wordcount:
    print(word, ":", wordcount[word])

