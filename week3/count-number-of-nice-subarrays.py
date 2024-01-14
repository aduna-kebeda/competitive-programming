class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        left = 0
        c = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                k -= 1
                cnt = 0
            l=left
            while k == 0:
                if nums[left] % 2:
                    k+=1
                left += 1
                cnt += 1

            c += cnt

        return c