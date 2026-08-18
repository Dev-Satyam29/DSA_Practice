class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq={}
        n=len(nums)
        for i in range(n-k+1):
            win=set(nums[i:i+k])
            for x in win:
                freq[x]=freq.get(x,0)+1
        ans=-1
        for k,v in freq.items():
            if freq[k]==1:
                ans=max(ans,k)
        return ans
        