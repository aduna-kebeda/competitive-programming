class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
       
        n=max([i[2] for i in trips])
       
        pre=[0]*(n+1)
        add=0
        for num in trips:
            pre[num[1]]+=num[0]
            pre[num[2]]-=num[0]
        add=0
     
      
        for i in range(n):
            add+=pre[i]
            if add>capacity:
                print(add)
                return False
             
        
        return True