class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]  
        c=0
        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                score = stack.pop()  
                stack[-1] += max(2 * score, 1) 
            print(stack)
        return stack[0]  
