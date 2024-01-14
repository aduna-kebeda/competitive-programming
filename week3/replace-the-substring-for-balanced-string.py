from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        left = 0
        cnt1 = Counter(s)
        replace = ""

        for char in cnt1:
            dif = cnt1[char] - n
            if dif > 0:
                replace += char * dif

        cnt2 = Counter(replace)
        mini = len(s)
        cnt3 = {}
        size=0
        for right in range(len(s)):
            if s[right] in cnt2:
                cnt3[s[right]] = cnt3.get(s[right], 0) + 1
                if cnt3[s[right]]==cnt2[s[right]]:
                   size+=1

            while size == len(cnt2) and left < len(s):
                mini = min(mini, right - left + 1)
                if s[left] in cnt3:
                    cnt3[s[left]] -= 1
                    if cnt3[s[left]] < cnt2[s[left]]:
                        size -= 1
                left += 1

            while left < right and s[left] not in cnt2:
                left += 1

        return 0 if replace == "" else mini