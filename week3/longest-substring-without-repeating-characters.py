class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        for i in range(len(s)):
            j=i
            store=set()
            while j<len(s):
                if s[j] not in store:
                    store.add(s[j])
                    j+=1
                else:
                    break

            maxi=max(maxi, len(store))
            if j==len(s):
                break
        return maxi