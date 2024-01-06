class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result={}
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            
            while left<right:
                if nums[left] + nums[right] + nums[i]==0:
    
                    if (nums[left], nums[right], nums[i]) not in result:
                       result[(nums[left], nums[right], nums[i])]=left
                       
                    if nums[right-1] ==nums[right]:
                        right-=1
                    elif nums[left] ==nums[left+1]:
                        left+=1
                    else:
                        left+=1
                        right-=1
                elif nums[left] + nums[right] +nums[i]>0:
                    right-=1
                elif nums[left] + nums[right] +nums[i]<0:
                    left+=1
        
        return result.keys()
                
                    

        