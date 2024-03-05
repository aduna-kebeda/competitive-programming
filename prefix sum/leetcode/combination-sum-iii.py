class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backTrack(start, total, sub):
            if total==n and len(sub)==k:
                result.add(tuple(sorted(sub[:])))
                return 
            
            if start>9 or total>n:
                return 

            for i in range(start, 10):
              
                sub.append(i)
                backTrack(i +1, total + i, sub)

                sub.pop()

        result=set()
        backTrack(1, 0, [])
        return [list(sub) for sub in result]
            