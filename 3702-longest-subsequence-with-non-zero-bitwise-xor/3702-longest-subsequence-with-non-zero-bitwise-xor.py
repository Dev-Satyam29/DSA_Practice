class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        non=False
        for n in nums:
            total=total^n
            if n!=0:
                non=True
        if total!=0:
            return len(nums)
        elif non:
            return len(nums)-1
        else:
            return 0
        