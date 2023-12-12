class Solution(object):
    def isHappy(self, n):
        num=int(n)
        if num==1:
            return True

        for i in range(20):
            s=str(num)
            temp=0
            for i in range(len(s)):
                temp+=int(s[i])**2
            num=temp
            if num==1:
                return True
        return False
            
            

            
            
        