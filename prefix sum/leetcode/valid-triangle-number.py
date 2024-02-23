class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        for r in range(len(nums) - 1, 1, -1):
            l = 0
            j = r - 1
            while l < j:
                if nums[l] + nums[j] > nums[r]:
                    cnt += j - l
                    j -= 1
                else:
                    l += 1
        return cnt
