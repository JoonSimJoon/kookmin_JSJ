import time
from DataBase import DataBase

def dbtesttime():
    start = time.time()
    DB = DataBase()
    DB.setScore()
    print("setScore %f time taken..", time.time()-start)
    start = time.time()
    DB.getstudentlist()
    print("getstudentlist %f time taken..", time.time()-start)
    start = time.time()
    for i in range(10):
        DB.addstudent("test" + str(i))
    print("addstudent %f time taken..", time.time()-start)
    start = time.time()
    DB.deletestudent("test1")
    print("deletestudent %f time taken..", time.time()-start)
    start = time.time()
    DB.setteachersays()
    print("setteachersays %f time taken..", time.time()-start)
    start = time.time()
    DB.getTeachersays()
    print("getTeachersays %f time taken..", time.time()-start)
    start = time.time()
    DB.setStudent_button()
    print("setStudent_button %f time taken..", time.time()-start)
    start = time.time()
    DB.getStudent_button()
    print("getStudent_button %f time taken..", time.time()-start)
    start = time.time()
    DB.compareData(0)
    print("compareData %f time taken..", time.time()-start)
    start = time.time()
    DB.getScore()
    print("getScore %f time taken..", time.time()-start)
    start = time.time()
    DB.getcurrentstage()
    print("getcurrentstage %f time taken..", time.time()-start)
    start = time.time()



if __name__ == "__main__":
    dbtesttime()
    
