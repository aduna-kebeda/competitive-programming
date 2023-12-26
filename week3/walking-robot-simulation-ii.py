
class Robot:

    def __init__(self, width: int, height: int):
        self.width=width-1
        self.height=height-1
        self.perimeter=2*(self.width +self.height)
        self.pos=[0, 0]
        self.dir="East"

    def step(self, num: int) -> None:
        num=num%self.perimeter   
        for i in range(num):
            if self.pos==[self.width, 0]:
                self.dir="North"
            elif self.pos==[self.width, self.height]:
                self.dir="West"
            elif self.pos==[0, self.height]:
                self.dir="South"
            elif self.pos==[0,0]:
                self.dir="East"

            if self.dir=="East":
                self.pos[0]+=1
            elif self.dir=="West":
                self.pos[0]-=1
            elif self.dir=="North":
                self.pos[1]+=1
            elif self.dir=="South":
                self.pos[1]-=1


        if self.pos==[0,0]:
                self.dir="South"

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()