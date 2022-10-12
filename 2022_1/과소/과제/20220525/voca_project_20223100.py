import traceback
import pickle 
import pandas as pd

def write_pickle(list_, path):
    with open(path, "wb") as f:
        pickle.dump(list_, f)
def read_pickle(path):
    with open(path, "rb") as f:
        return pickle.load(f)


try:
    dict_voca = {}
    with open("./voca.txt",mode="rt",encoding="utf-8" ) as f:
        for line in f:
            x = line.split(" /// ")
            dict_voca[x[0]] = x[1]
            print(x[0],x[1], dict_voca[x[0]])
    path = "voca.pkl"
    write_pickle(dict_voca, path)
    voca = pd.read_pickle(path)
    print(voca["absinth"])
except:
    traceback.print_exc()