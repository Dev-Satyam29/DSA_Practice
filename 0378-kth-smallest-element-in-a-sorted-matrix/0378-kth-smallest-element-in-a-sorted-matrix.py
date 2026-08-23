class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        row=n
        col=len(matrix[0])
        arr=[]
        for i in range(row):
            for j in range(col):
                arr.append(matrix[i][j])
        arr.sort()
        return arr[k-1]
