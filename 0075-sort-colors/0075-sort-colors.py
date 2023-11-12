class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            minIndex=i
            for j in range(i+1, len(nums)):
                if nums[j]<nums[minIndex]:
                    minIndex=j
            temp=nums[i]
            nums[i]=nums[minIndex]
            nums[minIndex]=temp
        return nums