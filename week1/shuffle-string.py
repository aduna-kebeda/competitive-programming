class Solution(object):
    def restoreString(self, s, indices):
        store = [""] * len(s)
        for i in range(len(s)):
            store[indices[i]] = s[i]
        return ''.join(store)
