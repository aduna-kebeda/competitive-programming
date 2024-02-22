class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        odd = 0

        for val in cnt.values():
            if val % 2 == 0:
                ans += val
            else:
                ans += val - 1
                odd = 1

        return ans + odd
