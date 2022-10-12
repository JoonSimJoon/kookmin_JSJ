dbfilename = 'test3_2.dat' #data 파일 이름 변수 설정

def readScoreDB():
    try: # 에러 캐치를 위한 try-except 문 설정
        fH = open(dbfilename) #파일 열기
    except FileNotFoundError as e:
        print("New DB: ", dbfilename) #파일 생성
        return []
    else:
        print("Open DB: ", dbfilename) #오픈한 데이터베이스 이름 출력

    scdb = []
    for line in fH: #한줄씩 분석
        dat = line.strip() # 공백문자 제거
        person = dat.split(",") #, 기준으로 문자열 분해
        record = {} #dictionary 생성
        for attr in person: 
            kv = attr.split(":") # : 기준으로 분해 (key, val)
            record[kv[0]] = kv[1]
        scdb += [record]
    fH.close() #파일 닫기
    return scdb # 값 리턴


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'w') # db 오픈
    for p in scdb: 
        pinfo = [] #list 생성
        for attr in p:
            pinfo += [attr + ":" + p[attr]]  #db에 학생정보 추가
        line = ','.join(pinfo)  #, 추가
        fH.write(line + '\n') #줄바꿈 추가
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > ")) #명령문 입력
        if inputstr == "": continue #엔터 입력시 재시도
        parse = inputstr.split(" ") # 띄어쓰기 기준으로 분해
        if parse[0] == 'add': #추가 시
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]} # 값들 정리해서
            scdb += [record] #학생 db에 추가
        elif parse[0] == 'del':
            for p in scdb: #삭제 시
                if p['Name'] == parse[1]: #이름 입력 받아서 삭제
                    scdb.remove(p)    
                    break
        elif parse[0] == 'show': #출력
            sortKey ='Name' if len(parse) == 1 else parse[1] #이름 탐색
            showScoreDB(scdb, sortKey) # 출력
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)