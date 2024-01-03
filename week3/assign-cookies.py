class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        p1=0
        p2=0
        cnt=0
        g.sort()
        s.sort()
        while p1<len(g) and p2<len(s):
            if g[p1] > s[p2]:
                p2+=1
                continue
            if s[p2] >= g[p1]:
                cnt+=1
            p1+=1
            p2+=1
        return cnt
