class Solution(object):
    def arrayChange(self, nums, operations):
        dic = {value: inde for inde, value in enumerate(nums)}
        for a, b in operations:
            nums[dic[a]] = b
            dic[b] = dic[a]
        return nums
