class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.count={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.count[tokenId] = currentTime + self.timeToLive

        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.count:
            if self.count[tokenId]>currentTime:
                self.count[tokenId] = currentTime + self.timeToLive
        
     
    def countUnexpiredTokens(self, currentTime: int) -> int:
        c = 0
        for token_time in self.count.values():
            if token_time > currentTime:
                c += 1
        return c
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)