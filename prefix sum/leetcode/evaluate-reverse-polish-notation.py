class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i].isnumeric() or (tokens[i][0] == '-' and tokens[i][1:].isnumeric()):
                stack.append(int(tokens[i]))
            elif len(stack) > 1:
                num1 = stack.pop()
                num2 = stack.pop()
                operator = tokens[i]

                if operator == '+':
                    stack.append(num2 + num1)
                elif operator == '-':
                    stack.append(num2 - num1)
                elif operator == '*':
                    stack.append(num2 * num1)
                elif operator == '/':
                    stack.append(int(num2 / num1))

        return stack[0]
