class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
       

    def push(self, val: int) -> None:
        mini=min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(mini)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()