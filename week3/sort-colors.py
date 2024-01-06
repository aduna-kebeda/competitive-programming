class Solution(object):
    def sortColors(self, nums):
        p=0
        for i in range(len(nums)):
            if nums[i]==0 :
                nums[i], nums[p]=nums[p], nums[i]
                p+=1
        
       
        for i in range(p, len(nums)):
            if nums[i]==1:
                nums[i], nums[p]=nums[p], nums[i]
                p+=1
        return nums