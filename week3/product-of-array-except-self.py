class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt=0
        pro=1
        zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
               pro*=nums[i]
            else:
               zero+=1 
        arr=[0]*len(nums)
        for i in range(len(nums)):
            if zero==1:
                if nums[i]==0:
                    arr[i]=int(pro)
                else:
                    arr[i]=0
            elif zero>1:
                arr[i]=0
            else:
                arr[i]=int(pro/nums[i])
                
        return arr
            

        