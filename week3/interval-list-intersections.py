class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(firstList) and p2 < len(secondList):
            a = max(firstList[p1][0], secondList[p2][0])
            b = min(firstList[p1][1], secondList[p2][1])
            if a <= b:
                result.append([a, b])
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return result