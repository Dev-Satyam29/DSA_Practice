class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        row=len(grid)
        col=len(grid[0])
        flag=True
        for i in range(row):
            for j in range(col):
                if (j==i or j==row-i-1) and grid[i][j]==0:
                    flag=False
                if (j!=i and j!=row-i-1) and grid[i][j]!=0:
                    flag=False
        return flag
        