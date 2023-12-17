from typing import List

class ATM:

    def __init__(self):
        self.dollar = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        self.check = {0: 500, 1: 200, 2: 100, 3: 50, 4: 20}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.dollar[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        temp = amount
        result = [0, 0, 0, 0, 0]

        for i in range(5):
            div = temp // self.check[i]
            mini = min(self.dollar[4-i], div)
            self.dollar[4-i] -= mini
            result[4-i] = mini
            temp -= self.check[i] * mini

        if temp == 0:
            return result
        else:
            for i in range(5):
                self.dollar[4-i] += result[4-i]
            return [-1]