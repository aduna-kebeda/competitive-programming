class Solution(object):
    def runningSum(self, nums):
        lst=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            lst.append(sum)

        return lst
