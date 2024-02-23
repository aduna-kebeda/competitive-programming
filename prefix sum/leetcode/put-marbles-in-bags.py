class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr=[]
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        return sum(arr[len(weights)-k:])-sum(arr[:k-1])


