class Solution:
    def minOperations(self, nums: List[int]) -> int:
        needed=0
        ans=0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                needed=nums[i-1]+1-nums[i]
                ans+=needed
                nums[i]=nums[i-1]+1
        return ans
        