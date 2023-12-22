class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix[0])):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        for k in range(len(matrix)):
            matrix[k]=matrix[k][::-1]
        return matrix
        