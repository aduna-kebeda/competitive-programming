class Solution(object):
    def mergeAlternately(self, word1, word2):
        string=""
        a=0
        b=0
        n=2*(min(len(word1), len(word2)))
        for i in range(n):
            if i%2==0:
                string += word1[a]
                
                a+=1
            else:
                string+=word2[b]
                b+=1
        length=len(word1)+len(word2)
        if len(word1)>len(word2):
            for i in range(n, length):
                string+=word1[a]
                a+=1
        elif len(word1)<len(word2):
            for i in range(n, length):
                string+=word2[b]
                b+=1
        return string
        
