class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mini=float('inf')
        size=len(cardPoints)-k
        add=0
        left=0
        for right in range(len(cardPoints)):
            add+=cardPoints[right]
            if right-left+1==size:
                mini=min(mini, add)
                add-=cardPoints[left]
                left+=1
            
        
        return sum(cardPoints)-mini if size>0 else sum(cardPoints)
                