class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        maxi=0
        processorTime.sort(reverse=True)
        tasks.sort()
        p1=0
        p2=3
        while p1<len(processorTime) and p2<len(tasks):
            maxi=max(processorTime[p1]+tasks[p2], maxi) 
            p1+=1
            p2+=4
        return maxi
        
        