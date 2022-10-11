import traceback
class Mat2D:
    def __init__(self, args):
        self.mat = args
        self.rows = len(args)
        self.cols = len(args[0])
        
    def __getitem__(self, args):
        return self.mat[args[0]][args[1]]
    def __add__(self, other):
        newmat = []
        try:
            for i in range(self.rows):
                x=[]
                for j in range(self.cols):
                    x.append(self[i][j]+other[i][j])
                newmat.append(x)
            return newmat
        except Exception as e:
             traceback.print_exc(e)
            
        
    def __sub__(self, other):
        newmat = []
        try:
            for i in range(self.rows):
                x=[]
                for j in range(self.cols):
                    x.append(self[i][j]-other[i][j])
                newmat.append(x)
            return newmat
        except Exception as e:
             traceback.print_exc(e)
    def __mul__(self, other):
        newmat = []
        try:
            for i in range(self.rows):
                x=[]
                for j in range(self.cols):
                    x.append(self[i][j]*other[i][j])
                newmat.append(x)
            return newmat
        except Exception as e:
             traceback.print_exc(e)
    def __str__(self):
        return self.mat

