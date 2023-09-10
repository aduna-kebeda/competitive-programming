class Solution(object):
    def checkInclusion(self, s1, s2):
        p = len(s1)
        s1=sorted(s1)
        for i in range(len(s2) - p + 1):
            str2=s2[i:i+len(s1)]
            str2=sorted(str2)
            if str2==s1:
                return True
            
        return False