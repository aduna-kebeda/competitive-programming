class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        area=0
        while right>left:
            max_sum=min(height[left], height[right])*(right-left)
            if max_sum>area:
                area=max_sum

            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return area


            
            
