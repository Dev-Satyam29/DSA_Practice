class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                maximum = 0
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        maximum = max(maximum, grid[x][y])
                ans[i][j] = maximum
        return ans