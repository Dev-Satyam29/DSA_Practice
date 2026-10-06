class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        total=0
        for key,v in freq.items():
            if freq[key]%k==0:
                total+=key*v
        return total
        