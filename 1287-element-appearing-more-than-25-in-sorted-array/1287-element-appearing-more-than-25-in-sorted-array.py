class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        occ=n*(25/100)
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if freq[k]>occ:
                return k
        