class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
       
        cnt=1
        temp=points[0][1]
        for i in range(1, len(points)):
            if points[i][0]>temp :
                cnt+=1
                temp=points[i][1]
                

        return cnt