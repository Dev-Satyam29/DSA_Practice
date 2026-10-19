class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        small=0
        equal=0
        res=[]
        for i in nums:
            if i<target:
                small+=1
            elif i==target:
                equal+=1
        for i in range(small,small+equal):
            res.append(i)
        return res
        