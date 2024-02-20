class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=defaultdict(int)
        for i in range(len(s)):
            dic[s[i]]=i
       
        arr=[]
        l=0
        maxi=0
        for r in range(len(s)):
            maxi=max(maxi, dic[s[r]])
            if maxi ==r:
                arr.append(r-l+1)
                l=r+1
        return arr






