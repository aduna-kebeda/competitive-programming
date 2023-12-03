class Solution(object):
    def checkPowersOfThree(self, n):
        
     num=int(math.log(n, 3))
     add=0
     for i in range(num, -1, -1):
         c=add+3**i
         if c<=n:
            add+=3**i
         print(add, i)
         if add==n:
             return True
         
    
     return False


