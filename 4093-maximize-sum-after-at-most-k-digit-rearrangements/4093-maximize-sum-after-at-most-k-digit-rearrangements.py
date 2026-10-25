class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        return sum(nums) + sum(sorted(
            int(''.join(sorted(str(num))[::-1])) - num
            for num in nums
        )[-k:])