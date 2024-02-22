class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        else:

            lst=list(palindrome)
            for i in range(len(lst)//2):
                if lst[i]!='a':
                    lst[i]='a' 
                    break 
            else:
                lst[-1]='b'
                 
        return "".join(lst)   
            