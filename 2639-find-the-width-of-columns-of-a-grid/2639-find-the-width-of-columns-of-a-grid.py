class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        if not grid or not grid[0]:
            return []
        res=[]
        for col in range(len(grid[0])):
            max_width=0
            for row in range(len(grid)):
                curr=len(str(grid[row][col]))
                max_width=max(curr,max_width)
            res.append(max_width)
        return res
        