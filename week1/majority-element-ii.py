class Solution(object):
    def majorityElement(self, nums):
        check=int(len(nums)/3)
        result=[]
        count=Counter(nums)
        for i in range(len(nums)):
            if count[nums[i]]>check and nums[i] not in result:
                result.append(nums[i])
        return result

        