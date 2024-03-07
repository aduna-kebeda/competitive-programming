class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right= x
       
        ans =0
        while left <= right:
            mid = (left + right)//2
            if mid**2 > x:
                right= mid-1
            elif  mid**2 <= x:
                left = mid + 1
                ans=mid
            
                
        
        return ans
