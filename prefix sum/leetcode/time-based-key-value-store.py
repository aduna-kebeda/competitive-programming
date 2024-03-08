class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)
        self.time =defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append(value)
        self.time[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        ind = bisect_right(self.time[key], timestamp)
        if ind==0:
            return ""
        return self.dic[key][ind-1]

        
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)