class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
       def isCapacity(total):
           temp=0
           day=0
           for num in weights:
               if num + temp > total:
                   day+=1
                   temp=0
               if num >total:
                   return 0
               temp += num
           day+=1
           return day <= days


       low=1
       high=sum(weights)
       while low <= high:
           mid=low + (high - low)//2
           if isCapacity(mid):
               high= mid -1
           else:
                low = mid +1

       return low
