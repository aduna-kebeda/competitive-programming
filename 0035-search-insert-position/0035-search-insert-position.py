class Solution(object):
    def searchInsert(self, nums, target):
        if len(nums)==1:
                if target<=nums[0]:
                    return 0
                else:
                    return 1
        for i in range(len(nums)):
            
            
            if nums[i]>=target:
                return i

            elif i==len(nums)-1 and target>nums[i]:
                return len(nums)
        return 
        