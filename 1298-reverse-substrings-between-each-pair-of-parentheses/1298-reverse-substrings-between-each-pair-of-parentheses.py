class Solution(object):
    def reverseParentheses(self, s):
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i].isalpha():
                stack.append(s[i])
            elif s[i]==')':
                store=""
                while stack[-1]!='(':
                    store+=stack.pop()
                stack.pop()
                for i in range(len(store)):
                    stack.append(store[i])
        stack=''.join(stack)
        return stack
