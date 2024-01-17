class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt=0
        dic=defaultdict(int)
        dic[0]=1
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            if add%k in dic:
                cnt+=dic[add%k]
            dic[add%k]+=1
            
        return cnt
