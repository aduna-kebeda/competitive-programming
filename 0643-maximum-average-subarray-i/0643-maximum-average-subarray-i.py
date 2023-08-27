class Solution(object):
    def findMaxAverage(self, nums, k):
         count = sum(nums[:k])  
         maxi = count /float(k)
         for i in range(k, len(nums)):
             count= count - nums[i - k] + nums[i]
             
             if count/float(k)>maxi:
                 maxi=count/float(k)

         return maxi
