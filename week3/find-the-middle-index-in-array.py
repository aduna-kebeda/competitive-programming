class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pre= 0
        for i in range(len(nums)):
            if pre== (total- pre - nums[i]):
                return i
            pre += nums[i]
        return -1