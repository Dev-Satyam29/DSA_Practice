class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [i * i for i in nums]
        nums.sort()
        k=len(nums)//2
        return sum(nums[k:])-sum(nums[:k])

        