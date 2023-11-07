class Solution(object):
    def majorityElement(self, nums):
        maxi=nums.count(nums[0])
        sing = list(set(nums))
        
        value = nums[0]
        n=int(len(nums)/2)
        for i in range(len(sing)):
            c=nums.count(sing[i])
            if c>n and c>maxi:
                maxi=c
                value = sing[i]
        return value
        