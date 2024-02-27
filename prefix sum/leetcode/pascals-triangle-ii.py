class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]

        prev=self.getRow(rowIndex-1)

        result=[0]*(rowIndex+1)
        result[0]=1
        result[-1]=1
        for i in range(1, rowIndex):
            result[i]= prev[i-1] + prev[i]
        
        return result