class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        n = len(nums)
        count = 0
        while(jumps>0 and count < n-1):
            count += 1
            jumps -= 1
            if nums[count] > jumps:
                jumps = nums[count]
        if count == n-1:
            return True
        else:
            return False

        
        