class Solution(object):
    def diagonalSum(self, mat):
        result=0
        dic={}
        i=0
        j=0
        while i<len(mat) and j<len(mat[0]):
            result+=mat[i][j]
            dic[(i,j)]=mat[i][j]
            i+=1
            j+=1
        i=0
        j=len(mat[0])-1
        while i<len(mat) and j>-1:
            if (i, j) not in dic:
                result+=mat[i][j]  
            i+=1
            j-=1
        return result
        