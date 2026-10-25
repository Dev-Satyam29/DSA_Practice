class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        while k>0:
            ans+=nums[n-1]
            nums[n-1]+=1
            k-=1
        return ans
        