class Solution(object):
    def sortColors(self, nums):
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        
        index = 0
        
        for i in range(c0):
            nums[index] = 0
            index += 1
            
        for i in range(c1):
            nums[index] = 1
            index += 1
            
        for i in range(c2):
            nums[index] = 2
            index += 1
            
        return nums