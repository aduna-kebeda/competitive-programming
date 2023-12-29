class Solution:
    def largestNumber(self, nums: List[int]) -> str:
       
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                con1 = str(nums[j]) + str(nums[j+1])
                con2 = str(nums[j+1]) + str(nums[j])
                if con2 > con1:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        nums = list(map(str, nums)) 
        if set(nums) == {"0"}:
            return "0" 

        return "".join(nums)

        #         if j not in s:
                    
        #             if str(maxi)<str(nums[j]) :
                        
        #                maxi=nums[j]
        #                key=j    
        #     s.add(key)      
        #     result.append(str(maxi))
        # print("30" <"3")
                       
        # return "".join(result)
        
        


      

    









        # s=set()
        # result=[]
        # maxi=len(str(max(nums)))
        # for i in range(maxi):
        #     sel=0
        #     key=i
        #     for j in range(len(nums)):
        #         if len(str(nums[i]))>=i+1 and j not in s:
        #             sel=max(nums[j][i], sel)
        #             key=j
        #             s.add(j)
        #     result.append(arr[key])
        # print(result)
            
        # print(arr)
        return 0