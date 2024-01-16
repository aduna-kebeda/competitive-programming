class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = float('inf')
        add = 0
        left = 0
        for right in range(len(nums)):
            add += nums[right]
            while add >= target:
                mini = min(mini, right - left + 1)
                add -= nums[left]
                left += 1
        return mini if mini != float('inf') else 0