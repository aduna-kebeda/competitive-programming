class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left =float('inf')
        right = float('inf')
        for n in nums:
            if n <= left:
                left = n
            elif n <= right:
                right = n
            else:
                return True
        return False