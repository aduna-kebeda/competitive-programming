class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre=[0]*(n+1)
        for num in bookings:
            pre[num[0]-1]+=num[2]
              
            pre[num[1]]-=num[2]
        add=0
        print(pre)
        for i in range(n):
            add+=pre[i]
            pre[i]=add
        return pre[:-1]

        

        