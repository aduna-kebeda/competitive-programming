class Solution(object):
    def lengthOfLongestSubstring(self, s):
        str2=[]
        f=0
        while f<len(s) and s[f] not in str2:
            str2.append(s[f])
            f=f+1
        lng=len(str2)
        for i in range(len(s)):
            str1=[]
            j=i
            while j<len(s) and s[j] not in str1 :
                str1.append(s[j])
                j=j+1
            if len(str1)>lng:
                lng=len(str1)

        return lng
