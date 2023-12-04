class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        i=0
        while i<(len(nums)):
            if nums[i]==1:
                count=0
                while i<len(nums) and nums[i]==1:
                    count+=1
                    i+=1
                if count>maxi:
                    maxi=count
            else:
                i+=1
            
        return maxi
