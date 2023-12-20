class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lst=[list(string) for string in strs]
        z=list(zip(*lst))
        count=0
        for sub in z:
            sub=list(sub)
            prev=sub[0]
            for i in range(1, len(sub)):
                if prev> sub[i]:
                    count+=1
                    break
                else:
                    prev=sub[i]
        return count



        return 0