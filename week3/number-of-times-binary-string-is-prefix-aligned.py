class Solution(object):
    def numTimesAllBlue(self, flips):
        cnt=0
        maxi=1
        for i in range(len(flips)):
            maxi=max(flips[i], maxi)
            if i>=maxi-1:
                cnt+=1
        return cnt


        