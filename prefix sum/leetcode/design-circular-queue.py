class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [None] * k  
        self.front = -1
        self.rear = -1
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
            self.rear = (self.rear + 1) % self.k
            self.que[self.rear] = value
            self.size += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.k
            self.size -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.que[self.front]
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.que[self.rear]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
