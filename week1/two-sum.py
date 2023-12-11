class Solution(object):
    def twoSum(self, nums, target):
        result=[]
        dic={}
        for i in range(len(nums)):
            find=target- nums[i]
            if find in dic:
                result.append(dic[find])
                result.append(i)
                return result
            else:
                dic[nums[i]]=i
        return result

        