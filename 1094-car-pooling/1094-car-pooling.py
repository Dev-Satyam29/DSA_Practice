class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tripc=[0 for _ in range(1001)]
        for trip,i,j in trips:
            tripc[i]+=trip
            tripc[j]-=trip
        carload=0
        for i in range(len(tripc)):
            carload+=tripc[i]
            if carload>capacity:
                return False
        return True
        