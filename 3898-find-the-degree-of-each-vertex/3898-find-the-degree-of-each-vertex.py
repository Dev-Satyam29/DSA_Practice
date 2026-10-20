class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        arr=[0]*n
        for i in range(n):
            for j in range(len(matrix[0])):
                arr[i]+=matrix[i][j]
        return arr
        