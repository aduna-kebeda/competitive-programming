class Solution:
    def maxVowels(self, s: str, k: int) -> int:
       check={'a', 'e', 'i', 'o', 'u'}
        
       cnt=0
       for j in range(k):
               if s[j] in check:
                   cnt+=1
       maxi=cnt
       for i in range(k, len(s)):
           if s[i-k] in check:
               cnt-=1
           if s[i] in check:
               cnt+=1
           maxi=max(maxi, cnt)
           
       return maxi
    