class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        j=1
        n=len(boxTypes)
        boxTypes.sort(key=lambda x:x[j],reverse=True)
        ans=0
        for i,j in boxTypes:
            take=min(i,truckSize)
            ans+=take*j
            truckSize-=take
            if truckSize==0:
                break
        return ans


        