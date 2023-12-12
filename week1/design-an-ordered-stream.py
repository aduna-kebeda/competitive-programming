class OrderedStream(object):

    def __init__(self, n):
        self.n = n
        self.operation=[""]*self.n 
        self.pointer=0

    def insert(self, idKey, value):
        self.operation[idKey - 1] = value
        result=[]
        if self.pointer<idKey-1:
            return []
        else:
            while self.pointer<self.n and self.operation[self.pointer]!="":
                result.append(self.operation[self.pointer])
                self.pointer+=1
            return result

            
                



        


# Your OrderedStream object will be instantiated and called as such:

#obj = OrderedStream(n)
#param_1 = obj.insert(idKey,value)