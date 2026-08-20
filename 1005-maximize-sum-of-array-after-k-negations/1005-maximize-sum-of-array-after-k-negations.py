class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        while i<n and nums[i]<0 and k>0:
            nums[i]=-nums[i]
            k-=1
            i+=1
        if k%2==1:
            nums.sort()
            nums[0]=-nums[0]
        return sum(nums)

        