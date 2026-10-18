class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        k=len(original)
        if m*n!=k:
            return []
        mat=[]
        for i in range(m):
            mat.append(original[i*n:(i+1)*n])
        return mat
        