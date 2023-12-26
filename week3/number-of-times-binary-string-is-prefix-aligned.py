class Solution(object):
    def numTimesAllBlue(self, flips):
        pointer=0
        cnt=0
        maxi=1
        lst=[0]*len(flips)
        for i in range(len(flips)):
            maxi=max(flips[i], maxi)
            if i>=maxi-1:
                cnt+=1
        return cnt


        