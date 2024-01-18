class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
       
        dic=defaultdict(int)
        dic[0]=1
        cnt=0
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            if add-goal in dic:
                cnt+=dic[add-goal]
            dic[add]+=1
        return cnt
