class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            curr=max(curr+nums[i],nums[i])
            total=max(total,curr)
        return total
        