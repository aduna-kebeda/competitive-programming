class Solution(object):
    def isPalindrome(self, s):
     
        lst = ""

       
        for char in s:
            
            if char.isalnum():
               
                lst += char.lower()

        
        return lst == lst[::-1]
