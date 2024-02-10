class Solution:
    def minimumSteps(self, s: str) -> int:
        p1 = 0
        cnt = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == '0':
                cnt += i - p1
                s[p1], s[i] = s[i], s[p1]
                p1 += 1
        return cnt