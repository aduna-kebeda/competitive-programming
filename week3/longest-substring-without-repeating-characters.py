class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        maxi = 0
        for right in range(len(s)):
            if s[right] in dic and dic[s[right]] >= left:
                left = dic[s[right]] + 1
            dic[s[right]] = right
            maxi = max(maxi, right - left + 1)
        return maxi