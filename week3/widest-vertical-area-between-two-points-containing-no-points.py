class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        cnt=0
        points.sort()
        for i in range(1,len(points)):
            prev=points[i-1][0]
            cnt=max(points[i][0]-prev, cnt)
        return cnt