class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt=0
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]<target:
                    cnt+=1
        return cnt

