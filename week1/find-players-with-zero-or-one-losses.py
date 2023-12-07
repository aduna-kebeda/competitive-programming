class Solution(object):
    def findWinners(self, matches):
        win=set()
        lost=set()
        count={}
        for match in matches:
            win.add(match[0])
            lost.add(match[1])
            count[match[1]]=count.get(match[1],0)+1
        oneloose=sorted([i for i in count if count[i]==1])
        return [sorted(list(win-lost)),oneloose]

        