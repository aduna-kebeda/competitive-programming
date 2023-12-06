class Solution(object):
    def pivotArray(self, nums, pivot):
        less=[]
        great=[]
        equal=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less.append(nums[i])
            elif nums[i]>pivot:
                great.append(nums[i])
            else:
                equal.append(nums[i])
        for j in range(len(equal)):
            less.append(equal[j])
        for k in range(len(great)):
            less.append(great[k])
        return less
        