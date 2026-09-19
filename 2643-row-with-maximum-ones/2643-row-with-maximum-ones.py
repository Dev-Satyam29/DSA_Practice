class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        freq={}
        maxi=0
        row=len(mat)
        col=len(mat[0])
        for i in range(row):
            count=0
            for j in range(col):
                if mat[i][j]==1:
                    count+=1
            if count not in freq:
                freq[count]=i
            maxi=max(maxi,count)
        arr=[]
        arr.append(freq[maxi])
        arr.append(maxi)
        return arr

        