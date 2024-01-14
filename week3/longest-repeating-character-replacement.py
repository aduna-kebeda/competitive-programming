class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left = 0
        maxi = 0

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            w = right - left + 1

            if w - max(dic.values()) <= k:
                maxi = max(w, maxi)
            else:
                while left < right and w - max(dic.values()) > k:
                    dic[s[left]] -= 1
                    left += 1
                    w -= 1

        return maxi