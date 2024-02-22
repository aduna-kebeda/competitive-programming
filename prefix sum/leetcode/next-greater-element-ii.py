class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        stack = []
        n = len(nums)
        
        for i in range(2 * n):
            idx = i % n
            while stack and nums[idx] > nums[stack[-1]]:
                num = stack.pop()
                dic[num] = nums[idx]
            stack.append(idx)
        
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            if i in dic:
                ans[i] = dic[i]
        
        return ans
