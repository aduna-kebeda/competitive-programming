class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string=str(num)
        cnt=0
        i=0
        while i<len(string)-k+1:
            if int(string[i:i+k])!=0 and num%int(string[i:i+k])==0:
                cnt+=1
            i+=1
        return cnt
