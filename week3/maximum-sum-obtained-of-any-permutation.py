class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        add=0
        pre=[0]*(len(nums)+1)
        for num in requests:
            pre[num[0]]+=1
            pre[num[1]+1]-=1
        for i in range(len(nums)):
            add+=pre[i]
            pre[i]=add
        
        pre.sort(reverse=True)
        i=0

        res=0
        nums.sort(reverse=True)
        while pre[i]>0 and i<len(nums):
            res+=pre[i]*nums[i]
            i+=1
        return res % (10**9 + 7)