class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mini= float('inf')
        re=0
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                dif=abs(nums[i]+ nums[left]+ nums[right]-target)
                if dif<mini:
                    mini=dif
                    re=nums[i]+ nums[left]+ nums[right]

                
                if nums[i]+ nums[left]+ nums[right]>target:
                    right-=1
                else:
                    left+=1
        return re