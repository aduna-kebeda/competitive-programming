class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        cnt=0
     
        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                
                top=stack.pop()
                if not stack: 
                    break
                width = i - stack[-1] - 1
                cnt+=(min(height[stack[-1]], height[i])-height[top]) * width
                
            stack.append(i)
        
        return cnt