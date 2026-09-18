class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        winner=0
        for i in range(n):
            if i==winner:
                continue
            if grid[winner][i]==0:
                winner=i
        return winner
        