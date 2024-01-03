class Solution(object):
    def sortSentence(self, s):
       s=list(s.split())
       re=[""]*(len(s))
       for string in s:
           inde=int(string[len(string)-1])
           re[inde-1]=string[:len(string)-1]
       return " ".join(re)
        