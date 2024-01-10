class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result=[]
        left=0
        right=len(p)
        cnt1=Counter(p)
        cnt2=Counter(s[:right])
        if cnt1==cnt2:
            result.append(left)
        n=len(p)
        for right in range(len(p), len(s)):
            cnt2[s[right-n]]-=1
            cnt2[s[right]]+=1
            if cnt2[s[right-n]]<=0:
                cnt2.pop(s[right-n])
            if cnt2==cnt1:
                result.append(right-n+1)

        return result
 



