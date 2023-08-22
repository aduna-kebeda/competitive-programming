class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr = []
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c = c + 1
            arr.append(c)
        
        return arr