class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que1=deque()
        que2=deque()
        for s in range(len(senate)):
            if senate[s]=="R":
                que2.append([senate[s],s])
            else:
                que1.append([senate[s],s])
        
        while que1 and que2:
            if que1[0][1] < que2[0][1]:
                que2.popleft()
                que1[0][1]+=len(senate)
                que1.append(que1.popleft())
                if not que2:
                    return "Dire"
            else:
                que1.popleft()
                que2[0][1]+=len(senate)
                que2.append(que2.popleft())
                if not que1:
                    return "Radiant"
        return "Dire" if que1 else "Radiant"
        