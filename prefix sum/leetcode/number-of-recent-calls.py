class RecentCounter:

    def __init__(self):
        self.que=deque()

    def ping(self, t: int) -> int:
        self.que.append(t)
        mini=t-3000
        while self.que and self.que[0]<mini:
            self.que.popleft()

        return len(self.que)
