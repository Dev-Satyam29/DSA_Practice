class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y + k):
            top = x
            bottom = x + k - 1
            while top < bottom:
                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]
                top += 1
                bottom -= 1
        return grid