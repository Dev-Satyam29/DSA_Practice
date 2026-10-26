class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums=[sorted(row,reverse=True) for row in nums]
        res=0
        for i in range(len(nums[0])):
            m=0
            for row in nums:
                m=max(m,row[i])
            res+=m
        return res