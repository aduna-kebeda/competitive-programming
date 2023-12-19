class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        dic={}
        for i in range(len(nums)):
            
            if nums[i] in dic:
               ind=dic[nums[i]]
               for j in range(len(ind)):
                   if (i*ind[j])%k==0:
                       count+=1
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)

        return count
