class Solution(object):
    def longestConsecutive(self, nums):
        dic={}
        maxi=0
        if len(nums)>0:
            maxi=1
        nums.sort()
        for i in range(len(nums)):
            if nums[i]-1 in dic:
                dic[nums[i]]=dic[nums[i]-1]+1
                if dic[nums[i]]>maxi:
                    maxi=dic[nums[i]]
            else:
                dic[nums[i]]=1
        return maxi
                 

        