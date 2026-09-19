class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visit=set()
        arr=[]
        arr1=[]
        row=len(grid)
        col=len(grid[0])
        for i in range(1,row**2+1):
            arr.append(i)
        for i in range(row):
            for j in range(col):
                if grid[i][j] in visit:
                    arr1.append(grid[i][j])
                else:
                    visit.add(grid[i][j])
        for i in arr:
            if i not in visit:
                arr1.append(i)
        return arr1
        
        