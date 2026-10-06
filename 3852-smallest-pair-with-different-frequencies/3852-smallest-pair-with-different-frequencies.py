class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        min_ele=min(freq)
        res=[-1]*2
        min_ele2=float('inf')
        for k,v in freq.items():
            if k>min_ele and v!=freq[min_ele]:
                min_ele2=min(min_ele2,k)
        if min_ele2!=float('inf'):
            res[0]=min_ele
            res[1]=min_ele2
        return res

        