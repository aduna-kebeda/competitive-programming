class Solution(object):
    def moveZeroes(self, nums):
       left=0
       right=0
       while right<len(nums):
           if nums[right]!=0:
               nums[right], nums[left]=nums[left], nums[right]
           if nums[left]!=0:
                left+=1
           right+=1
           
               
        