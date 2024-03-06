class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ans = 0
        k -= 1
        while k:
            if k%2:
                ans += 1
            k//=2
        return ans %2
