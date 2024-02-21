class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        result=1
        cnt=0
        while target>1:
            if maxDoubles<=0:
                cnt+=target-1
                return cnt
            if target%2==0 and maxDoubles>0:
                cnt+=1
                maxDoubles-=1
                target//=2
            else:
                target-=1
                cnt+=1 

        return cnt             
       
       