class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        arr=[]
        for i in range(len(nums)):
            arr.append(nums[i])
        for i in range(len(nums)-1,0,-1):
            arr.append(nums[i])
        arr.append(nums[0])
        return arr
        