class Solution(object):
    def largestGoodInteger(self, num):
        maxi=-1
        i=0
        while i<(len(num)-2):
            if len(set(num[i:i+3]))==1:
                print(num[i:i+3])
                if int(maxi)<int(num[i:i+3]):
                    maxi=num[i:i+3]
                    i+=3
                    
                    continue
            i+=1
        if maxi!=-1:
           return maxi
        else:
            return ""
        
        