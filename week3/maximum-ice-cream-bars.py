class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cnt=0
        costs.sort()
        i=0
        while i<len(costs):
            cnt+=costs[i]
            if cnt>coins:
                cnt-=costs[i]
                break
            i+=1
        return i


       