class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        que=deque()
        deck.sort(reverse=True)
        for i in range(len(deck)):
            if que:
                que.appendleft(que.pop())
            que.appendleft(deck[i])
        return que

        