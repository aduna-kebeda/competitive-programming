class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        self.ans = ""
        def check(string):
            counter = Counter(string)
            if all(counter[i.upper()] >=1 and  counter[i.lower()]>=1  for i in counter):
                self.ans = string
                return 1
        for w in range(len(s),-1,-1):
            for i in range(0,len(s)- w + 1):
            
                if check(s[i:i+w]):return self.ans
        return ""

            