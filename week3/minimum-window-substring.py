class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt1 = Counter(t)
        cnt2 = {}
        formed = 0
        i = 0
        j = len(s) - 1
        left = 0
        window_found = False
        for right in range(len(s)):
            if s[right] in cnt1:
                cnt2[s[right]] = cnt2.get(s[right], 0) + 1
                if cnt2[s[right]] == cnt1[s[right]]:
                    formed += 1

            while formed == len(cnt1):
                window_found = True
                if right - left < j - i:
                    i, j = left, right
                if s[left] in cnt2:
                    cnt2[s[left]] -= 1
                    if cnt2[s[left]] < cnt1[s[left]]:
                        formed -= 1
                left += 1
        return "" if not window_found else s[i:j+1]