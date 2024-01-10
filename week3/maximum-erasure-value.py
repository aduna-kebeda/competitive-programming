class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result=0
        left=0
        dic={}
        add=0
        for right in range(len(nums)):
            if nums[right] in dic and dic[nums[right]]>=left:
                for i in range(left,dic[nums[right]]):
                    add-=nums[i]
                left=dic[nums[right]]+1
            else:
                add+=nums[right]
            dic[nums[right]]=right
            result=max(result, add)
        return result
            


            
        # while left<len(nums):
        #     dic={}
        #     add=0
        #     j=left
        #     while j<len(nums):
        #         if nums[j] not in dic:
        #             dic[nums[j]]=j
        #             add+=nums[j]
        #         else:   
        #             left=dic[nums[j]]+1
        #             break 
        #         j+=1
        #     result=max(add, result)
        #     if j==len(nums):
        #         break
                
        # return result   