class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
     
        def backtrack(first_num, path, n):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(first_num, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path, n)
                path.pop()
        
        ans = [[]] 
        for i in range(1, len(nums)+1):
           backtrack(0, [], i)
        return ans
