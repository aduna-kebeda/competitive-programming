class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        av=sum(nums[:k])/k
        cnt=sum(nums[:k])
        for i in range(k, len(nums)):
            cnt=cnt-nums[i-k]+ nums[i]
            av=max(av, cnt/k)
        return av

        