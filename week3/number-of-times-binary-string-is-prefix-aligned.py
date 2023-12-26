class Solution(object):
    def numTimesAllBlue(self, flips):
        pointer=0
        cnt=0
        maxi=1
        lst=[0]*len(flips)
        for i in range(len(flips)):
            lst[flips[i]-1]=1
            while pointer<len(flips) and lst[pointer]!=0:
                pointer+=1
            maxi=max(flips[i], maxi)
            if pointer>=maxi:
                cnt+=1
        return cnt


        