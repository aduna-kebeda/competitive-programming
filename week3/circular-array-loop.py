class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            j = 0
            k = i
            s = set()
            neti=True
            x=k
            for _ in nums:
                if nums[k]>0 and nums[x]<0:
                    neti=False
                    break
                elif  nums[k]<0 and nums[x]>0:
                    neti=False
                    break
                x+=nums[x]
                x=x%len(nums)
            if  neti:
                while j < len(nums):

                    if nums[k]%len(nums) != 0:
                        s.add(k)
                    k = (k + nums[k]) % len(nums)
                  
                    if  k in s  :
                        return True
                    j += 1
        return False
