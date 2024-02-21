class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op=0
    
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>nums[i+1]:
                x=math.ceil(nums[i]/nums[i+1])
                op+=x-1
                nums[i]=nums[i]//x
                
        return op
                    