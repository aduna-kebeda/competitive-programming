class Solution(object):
    def moveZeroes(self, nums):
        zero=nums.count(0)
        
        for i in range(zero):
            nums.remove(0)
        
        for i in range(zero):
            nums.append(0)
        return nums

        