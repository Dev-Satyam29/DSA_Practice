class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        freq={}
        row=len(mat)
        col=len(mat[0])
        for i in range(row):
            count=0
            for j in range(col):
                if mat[i][j]==1:
                    count+=1
            freq[i]=count
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1]))
        arr=[]
        count=0
        for key,val in sorted_dict.items():
            if count<k:
                arr.append(key)
                count+=1
        return arr
        