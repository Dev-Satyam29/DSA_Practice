class Solution:
    def minMoves(self, nums: list[int]) -> int:
        total=0
        for i in nums:
            total+=i
        min_ele=min(nums)
        return total-(min_ele*len(nums))
        