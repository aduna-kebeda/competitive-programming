class Solution(object):
    def pivotIndex(self, nums):
        pre_sum=[]
        if sum(nums)-nums[0]==0:
                return 0
        for i in range(len(nums)):
            pre_sum.append(sum(nums[0:i+1]))
        
        for j in range(1, len(pre_sum)):
            
            if pre_sum[j-1]==pre_sum[len(nums)-1]-pre_sum[j]:
                return j
        return -1
        

        