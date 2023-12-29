class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt=0
        nums.sort()
        i=len(nums)-2
        while i>-1:
            if nums[i]!=nums[i+1]:
                cnt+=len(nums)-1-i 
            i-=1
            
        return cnt
             

