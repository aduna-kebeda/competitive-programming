class Solution(object):
    def sumOfThree(self, num):
        

        f=int(num//3)-3
        lst=[]
        e= int(num//3)+3
        for i in  range(f, e):
            if i+(i+1)+(i+2)==num:
                
                lst.append(i)
                lst.append(i+1)
                lst.append(i+2)
                return lst
        return lst
        