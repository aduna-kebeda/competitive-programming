class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dic = []

        for i in range(len(points)):
            distance = (points[i][0]) ** 2 + (points[i][1]) ** 2
            dic.append([distance, i])
        
        dic.sort()
        r=[]
        for i in range(k):
            r.append(points[dic[i][1]])

        return r

        # for i in range(1, len(points)):
        #     j = i
        #     while j > 0 and dic[j - 1] > dic[j]:
        #         dic[j - 1], dic[j] = dic[j], dic[j - 1]
        #         points[j - 1], points[j] = points[j], points[j - 1]
        #         j -= 1

        
        