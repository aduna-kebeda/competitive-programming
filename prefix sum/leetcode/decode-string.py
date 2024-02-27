class Solution:
    def decodeString(self, s: str) -> str:
        self.idx=0


        def recurse():
            num=0
            res=""
            while self.idx<len(s):
                if s[self.idx].isdigit():
                    num=(num*10) + int(s[self.idx])
                    self.idx+=1
                elif s[self.idx]=='[':
                    self.idx+=1
                    res+=num*recurse()
                    num=0
                elif s[self.idx]==']':
                    self.idx+=1
                    return res
                else:
                    res+=s[self.idx]
                    self.idx+=1
            return res

        return recurse()
       






        # self.idx = 0
        # def recurse():
        #     num = 0
        #     res = ""
        #     while self.idx < len(s):
        #         if s[self.idx].isdigit():
        #             num = num * 10 + int(s[self.idx])
        #             self.idx += 1
        #         elif s[self.idx] == '[':
        #             self.idx += 1
        #             decoded_string = recurse()
        #             res += num * decoded_string
        #             num = 0
        #         elif s[self.idx] == ']':
        #             self.idx += 1
        #             return res
        #         else:
        #             res += s[self.idx]
        #             self.idx += 1
        #     return res

        # return recurse()