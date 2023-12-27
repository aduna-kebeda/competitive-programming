class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            j=i
            while j>0:
                if nums[j]<nums[j-1]:
                    nums[j], nums[j-1]=nums[j-1], nums[j]
                else:
                    break
                j-=1
        return nums