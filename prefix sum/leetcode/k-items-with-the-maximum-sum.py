class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        po=numOnes + numZeros
        if po>=k:
            if numOnes>k:
                return k
            else:
                return numOnes
        else:
            dif=k-po
            if dif <= numNegOnes:
                return po-dif-numZeros
