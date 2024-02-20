class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x :x[0]-x[1])
        half=len(costs)//2
        result =0
        for i in range(len(costs)//2):
            result+=costs[i][0]
            result+=costs[i+half][1]
       
        return result
        