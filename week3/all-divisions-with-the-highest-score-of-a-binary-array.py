class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        dic={}
        total=sum(nums)
        cnt=0
        for i in range(len(nums)+1):
            if i==len(nums):
               add=total-(i-cnt)+cnt
               if add in dic:
                  dic[add].append(i)
               else:
                   dic[add]=[i]
               break
           
            else:
                add=total-(i-cnt)+cnt
            if add in dic:
               dic[add].append(i)
            else:
               dic[add]=[i]
            if nums[i]==0:
                cnt+=1
     
        result=max(dic)
        return dic[result]