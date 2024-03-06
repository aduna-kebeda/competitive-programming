class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backTrack(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or row >= len(board) or
                col < 0 or col >= len(board[0]) or
                board[row][col] != word[index]):
                return False

            temp, board[row][col] = board[row][col], "/"
            result = (backTrack(row + 1, col, index + 1) or
                      backTrack(row - 1, col, index + 1) or
                      backTrack(row, col + 1, index + 1) or
                      backTrack(row, col - 1, index + 1))
            board[row][col] = temp
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backTrack(i, j, 0):
                    return True

        return False
