class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cnt = 0

        for i in range(len(nums)):
            if cnt < i:
                return False
            cnt = max(cnt, i + nums[i])

            if cnt >= len(nums) - 1:
                return True

        return False
