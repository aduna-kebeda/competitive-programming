class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        d=s.split(' ')
        f=d[-1]

       
        return len(f)
        