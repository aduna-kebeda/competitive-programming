class Solution(object):
    def shuffle(self, nums, n):
        sub=nums[n:]
        result=[]
        for i in range(n):
            result.append(nums[i])
            result.append(sub[i])
        return result
        