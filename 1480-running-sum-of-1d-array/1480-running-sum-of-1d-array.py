class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total_sum=0
        n=len(nums)
        for i in range(n):
            temp=nums[i]
            nums[i]=nums[i]+total_sum
            total_sum+=temp
        return nums
        