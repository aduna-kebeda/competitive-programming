class Solution(object):
    def removeDuplicates(self, nums):
        s=list(set(nums))
        for i in s:
            c=nums.count(i)
            if c>2:
                for j in range(c-2):
                    nums.remove(i)
        return len(nums)
        