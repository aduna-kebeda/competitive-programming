class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backTrack(start, sub, n, result):
            if len(sub) == n:
                result.add(tuple(sorted(sub)))
                return

            for i in range(start, len(nums)):
                sub.append(nums[i])
                backTrack(i + 1, sub, n, result)
                sub.pop()

        result = set()
        for i in range(1, len(nums) + 1):
            backTrack(0, [], i, result)

        return [list(subset) for subset in result]+ [[]]
