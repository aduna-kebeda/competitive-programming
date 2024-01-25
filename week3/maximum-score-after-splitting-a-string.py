class Solution:
    def maxScore(self, s: str) -> int:
        pre=[0]*(len(s)+1)
        add=0
        for  i in range(len(s)):
            add+=int(s[i])
            pre[i]=add
        maxi=0
        for i in range(len(s)-1):
          
            zero=i-pre[i]+1
            one=pre[len(s)-1]-pre[i]
            print(zero)
            maxi=max(maxi, zero+one)
        
        return maxi
        