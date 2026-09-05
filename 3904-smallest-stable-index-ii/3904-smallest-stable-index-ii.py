class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        min_array=[0]*n
        min_array[n-1]=nums[n-1]
        for i in range(1,n):
            min_array[n-i-1]=min(nums[n-i-1],min_array[n-i])
        maxi=nums[0]
        for i in range(n):
            maxi=max(maxi,nums[i])
            stability=maxi-min_array[i]
            if stability<=k:
                return i
        return -1