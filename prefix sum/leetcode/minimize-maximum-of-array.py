class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
      pre=0
      ans=nums[0]
      for i in range(len(nums)):
          pre+=nums[i]
          if  nums[i]>ans:
              ans=max(ans,ceil(pre/(i+1)))
      return ans 
      