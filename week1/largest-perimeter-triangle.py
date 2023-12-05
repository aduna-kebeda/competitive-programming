class Solution(object):
    def largestPerimeter(self, nums):
        maxi=0
        if len(nums)<3:
            return maxi
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2] and nums[i+2]+nums[i+1]>nums[i] and nums[i]+nums[i+2]>nums[i+1]:
                maxi=nums[i]+nums[i+1]+nums[i+2]
                return maxi
        
        
        return maxi
        