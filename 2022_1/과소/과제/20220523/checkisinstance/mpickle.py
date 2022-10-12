
import pickle

f = open("TextFile.txt", "w");
dic = pickle.load(f)
x = dic
print(x , type(x))
f.close()