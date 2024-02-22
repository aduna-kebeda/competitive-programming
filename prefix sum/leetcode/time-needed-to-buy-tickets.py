class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt=0
        for i in range(k):
            if tickets[i]>=tickets[k]:
                cnt+=tickets[k]
            else:
                cnt+=tickets[i]
        for i in range(k, len(tickets)):
            if tickets[i]>=tickets[k]:
                cnt+=tickets[k]-1
            else:
                cnt+=tickets[i]
        return cnt+1
        
