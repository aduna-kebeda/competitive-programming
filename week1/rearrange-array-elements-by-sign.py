class Solution(object):
    def rearrangeArray(self, nums):
        po=[]
        ne=[]
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                po.append(nums[i])
            else:
                ne.append(nums[i])
        n=len(nums)/2
        for i in range(n):
            result.append(po[i])
            result.append(ne[i])
        return result

        