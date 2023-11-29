class Solution(object):
    def longestCommonPrefix(self, strs):
        stack = []
        f = strs[0]
        for i in range(len(f)):
            stack.append(f[i])

        for string in strs:
            n=min(len(stack), len(string))
            if string=="":
                    return ""
            for i in range(n):
                d=stack
                p=''.join(d)
                if len(stack)>len(string) and p[:len(string)]==string:
                        while len(stack)>len(string):
                            stack.pop()
                elif f[i] != string[i]:
                    if not stack:
                        return ""
                    
                    else:
                        while len(stack) > i: 
                            stack.pop()

        return ''.join(stack)