class Solution(object):
    def isAnagram(self, s, t):
        bl = True
      
        if len(s) == len(t):
            for i in range(len(s)):
                if t[i] not in s or (s.count(t[i])!=t.count(t[i])):
                    bl = False
        else:
            bl = False

        return bl