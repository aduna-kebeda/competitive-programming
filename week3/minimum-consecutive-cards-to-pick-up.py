class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        mini=len(cards)
        for right in range(len(cards)):
            if cards[right] in dic:
                mini=min(mini, right-dic[cards[right]]+1)
            dic[cards[right]]=right 
        if len(set(cards))==len(cards):
            return -1
        return mini
            