class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=0
        c=k
        for right in range(len(answerKey)):
            if answerKey[right]=='F':
                c-=1
            if c<0:
                if answerKey[left]=='F':
                    c+=1
                left+=1
        maxi=right-left+1

        left=0
        for right in range(len(answerKey)):
            if answerKey[right]=='T':
                k-=1
            if k<0:
                if answerKey[left]=='T':
                    k+=1
                left+=1
        maxi=max(maxi, right-left+1)

        return maxi