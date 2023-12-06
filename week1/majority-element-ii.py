class Solution(object):
    def majorityElement(self, nums):
        check=int(len(nums)/3)
        result=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>check and nums[i] not in result:
                result.append(nums[i])
        return result

        