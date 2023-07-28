class Solution(object):
    def isPalindrome(self, s):

        s = s.strip()
        
        s = ''.join(c for c in s if c.isalnum())

        s= s.upper()
        r = s[::-1]
        if r==s:
            return True
        else:
            return False
