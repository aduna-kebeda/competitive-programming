class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        ans=-1
        while left <= right:
            mid=(left + right)//2
            l=0
            r=len(matrix[0])-1
            if matrix[mid][0] < target and matrix[mid][-1] >= target:
                
                while l <= r:
                    m=(l + r)//2
                    if matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        ans=[mid, m]
                        return True
                return False
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True
        return False
                
            

