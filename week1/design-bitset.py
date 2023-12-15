class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitzero = ['0' for _ in range(self.size)]
        self.bitone = ['1' for _ in range(self.size)]
        self.cnt=0

    def fix(self, idx: int) -> None:
        if self.bitzero[idx]=='0':
            self.bitzero[idx]='1'
            self.bitone[idx]='0'
            self.cnt+=1
        

    def unfix(self, idx: int) -> None:
       if  self.bitzero[idx]=='1':
      
            self.bitzero[idx]='0'
            self.bitone[idx]='1'
            if self.cnt>0:
                self.cnt-=1

    def flip(self) -> None:
        self.bitzero, self.bitone=self.bitone, self.bitzero
        self.cnt=self.size-self.cnt

    def all(self) -> bool:
        return self.cnt==self.size

    def one(self) -> bool:
        return self.cnt>0
        

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        return ''.join(self.bitzero)

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()