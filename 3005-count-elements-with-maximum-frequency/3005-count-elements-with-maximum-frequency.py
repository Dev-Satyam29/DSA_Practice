class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        max_freq=0
        for i in freq:
            max_freq=max(max_freq,freq[i])
        total=0
        for k,v in freq.items():
            if v==max_freq:
                total+=v
        return total

        