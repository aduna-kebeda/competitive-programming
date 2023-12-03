class Solution(object):
    def freqAlphabets(self, s):
        string=""

        i=0
        while i<(len(s)-2):
            if s[i]!='#' and s[i+2]!='#':
               char=chr(int(s[i])+64)
               char=char.lower()
               string+=char
               i+=1
            elif s[i]!='#' and s[i+2]=='#':
               char=chr(int(s[i:i+2])+64)
               char=char.lower()
               string+=char
               i+=3
        n=len(s)
        if s[n-2]!='#' and s[n-1]!='#':
             char=chr(int(s[n-2])+64)
             char=char.lower()
             string+=char
        if  s[n-1]!='#':
             char=chr(int(s[n-1])+64)
             char=char.lower()
             string+=char
        
        return string


            