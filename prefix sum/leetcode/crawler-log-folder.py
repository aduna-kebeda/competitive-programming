class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for op in logs:
            if stack and op=="../":
                stack.pop()
            elif op=="./":
                continue
            elif op!="../":
                stack.append(op)
        return len(stack)
