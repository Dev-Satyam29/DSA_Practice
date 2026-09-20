class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        freq={}
        row=len(matrix)
        col=len(matrix[0])
        for i in range(col):
            maxi=matrix[0][i]
            for j in range(row):
                maxi=max(matrix[j][i],maxi)
            freq[i]=maxi
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==-1:
                    matrix[i][j]=freq[j]
        return matrix
        
        