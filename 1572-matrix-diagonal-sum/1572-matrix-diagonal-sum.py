class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        count=0
        for i in range(n):
            count+=mat[i][i]
            count+=mat[i][n-i-1]
        if n%2==1:
            count-=mat[n//2][n//2]
        return count
        