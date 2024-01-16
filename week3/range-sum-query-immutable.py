class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.pre=[0]*len(nums)
        add=0
        for i in range(len(nums)):
            add+=self.nums[i]
            self.pre[i]=add
        
        print(self.pre)
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right]-self.pre[left]+self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)