class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        cnt=0
        for i in range(len(nums)):
            idx=bisect_right(nums, target-nums[i])
            if idx<= i:
                return cnt%(10**9 +(7))
            cnt += 2**(idx-i-1)
        return cnt%(10**9 +(7))
        

       
        