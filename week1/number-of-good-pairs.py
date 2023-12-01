class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(len(nums)-1):
           num=nums[i]
           count+=nums[i+1:].count(num)
        return count
        
        