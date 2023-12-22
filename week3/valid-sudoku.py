class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        z=list(zip(*board))
        for row in board:
           lst=[num for num in row if num.isnumeric()] 
           if len(lst)!=len(set(lst)):
               return False 
        for row in z:
           lst=[num for num in row if num.isnumeric()] 
           if len(lst)!=len(set(lst)):
               return False     
        for i in range(0,len(board[0])-2, 3):
            
            for j in range(0, len(board)-2, 3):
                lst=[]
                for k in range(i, i+3):
                    for r in range(j, j+3):
                        if board[k][r].isnumeric():
                           lst.append(board[k][r])
                if len(lst)!=len(set(lst)):
                    return False
        return True
