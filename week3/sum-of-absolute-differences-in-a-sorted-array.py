class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        pre=[0]*(len(nums)+1)
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            pre[i]=add
        arr=[0]*len(nums)
        arr[0]=pre[len(nums)-1] - (nums[0]*len(nums))
        print(pre)
        for i in range(1,len(nums)):
            size=len(nums)-i
            right=pre[len(nums)-1] - (nums[i]*size)-pre[i-1]
            left=(nums[i]*(i))-pre[i-1]
            if i==len(nums)-1:
                 arr[i]=left
            else:
                 arr[i]=right+left
        return arr
        