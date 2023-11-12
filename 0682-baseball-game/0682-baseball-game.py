class Solution(object):
    def calPoints(self, operations):
        stack=[]
        for i in range(len(operations)):
            
            
            if operations[i]=="C":
                stack.pop()
            elif operations[i]=="D":
                stack.append(stack[-1]*2)
            elif operations[i]=="+":
                top=stack.pop()
                prev=stack[-1]
                stack.append(top)
                stack.append(top+prev)
            else:
                stack.append(int(operations[i]))
            print(stack)
        return sum(stack)



        