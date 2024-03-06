class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def isPosible(k):
            temp=0
            cnt=0
            for banana in piles:
                cnt+= banana//k
                if banana%k:
                    cnt+=1
            
            return cnt <= h

        piles.sort()
        low=1
        high=sum(piles)
        while low <= high:
            mid=(high + low)//2
            if isPosible(mid):
                high= mid - 1
            else:
                low = mid + 1
            print(mid)
        return low
                