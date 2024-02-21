class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        close=0
        for i in range(len(s)):
            if s[i]=='(':
                open+=1
            else:
                if open>0:
                    open-=1
                else:
                    close+=1
                
        return open+close
