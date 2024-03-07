class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        ans=1
        for i in range(len(citations)+1):
            if i<=len(citations)- bisect_left(citations, i):
                ans=i
        return ans
