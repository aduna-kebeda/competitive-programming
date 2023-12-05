class Solution(object):
    def checkPossibility(self, nums):
        for i in range(len(nums)):
            num = nums[:]
            num.pop(i)
            
            if num == sorted(num):
                return True
            elif i>1 and num[i-2]>num[i-1]:
                print(i)
                return False
            
        return False
