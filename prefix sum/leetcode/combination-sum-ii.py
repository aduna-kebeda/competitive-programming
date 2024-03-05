class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        def backTrack(idx, total, sub):
            if total==target:
                result.add(tuple(sorted(sub[:])))
                return 
            
            if idx>=len(candidates) or total>target:
                return 

            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                sub.append(candidates[i])
                backTrack(i +1, total + candidates[i], sub)

                sub.pop()

        result=set()
        backTrack(0, 0, [])
        return [list(sub) for sub in result]
            