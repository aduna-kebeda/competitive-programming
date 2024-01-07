class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxi=0
        i=0
        while i<len(nums):
            j=i
            one=0
            zero=0
            store=[]
            while zero<2 and j<len(nums):
                one+=1
                if nums[j]==0:
                    store.append(j)
                    zero+=1
                j+=1
            if zero>0:
               i=store[0]+1
            if zero>0:
                maxi=max(maxi, one-zero)
            elif zero==0:
                maxi=max(maxi, one-1)
            if j==len(nums):
                break

        return maxi