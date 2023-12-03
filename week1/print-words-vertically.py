class Solution(object):
    def printVertically(self, s):
        s=s.split()
        maxi=len(s[0])
        inde=0
        for i in range(len(s)):
            if len(s[i])>maxi:
                maxi=len(s[i])
                inde=i
        string=[""]*maxi
        for st in s:
            i=0
            while i<len(st):
                   string[i]+=st[i]
                   i+=1
            
            for j in range(i, maxi):
                string[j]+=" "
        
        for i in range(len(string)):
            sub=string[i]
            for j in range(len(sub)-1, -1, -1):
                if sub[j]!=' ':
                    string[i]=sub[:j+1]
                    
                    break

            
        return string

            
        