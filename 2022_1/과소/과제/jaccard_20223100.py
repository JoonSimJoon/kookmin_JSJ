allSet=[{1,2,3,4,5,6,7,8,9,10}, {1,3,5,7,12,15}, {3,12,15,18,20},{12,13,14,15,16,17,18,19}]

for i in range(4):
    for j in range(i+1,4):
        inter = allSet[i] & allSet[j]
        uni = allSet[i] | allSet[j]
        print("(%d,%d) 집합의 자카트 지수: %d/%d" %(i+1,j+1,len(inter),len(uni)))

