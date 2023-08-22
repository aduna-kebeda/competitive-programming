class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ret=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ret.append(i)
                
        return ret
       
        