class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        z=list(zip(*grid))
        cnt=0
        col=[]
        row=[]
        for i in range(len(grid[0])):
            row.append(max(grid[i]))
        for j in range(len(grid)):
            col.append(max(z[j]))
        
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                mini=min(row[i],col[j])

                cnt+=mini-grid[i][j]
        return cnt