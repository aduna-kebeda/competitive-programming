class Solution(object):
    def decompressRLElist(self, nums):
       result=[]
       i=0
       while i<len(nums)-1:
           freq=nums[i]
           val=nums[i+1]
           for j in range(freq):
               result.append(val)
           i+=2
       return result
        