class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.pre = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.pre[(i, j)] = matrix[i][j]
                if i > 0:
                    self.pre[(i, j)] += self.pre[(i-1, j)]
                if j > 0:
                    self.pre[(i, j)] += self.pre[(i, j-1)]
                if i > 0 and j > 0:
                    self.pre[(i, j)] -= self.pre[(i-1, j-1)]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.pre[(row2, col2)]
        if row1 > 0:
            total -= self.pre[(row1-1, col2)]
        if col1 > 0:
            total -= self.pre[(row2, col1-1)]
        if row1 > 0 and col1 > 0:
            total += self.pre[(row1-1, col1-1)]
        return total