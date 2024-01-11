class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
       nums.sort(reverse=True)
       left=0
       cnt=0
       add=0
       for right in range(len(nums)):
           add+=nums[right]
           size=right-left+1
           pro1=add
           pro2=nums[left]*(size)
           if pro2-pro1<=k:
               cnt+=1 
           else:
               add-=nums[left]
               left+=1
       return cnt