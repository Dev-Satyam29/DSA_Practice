class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        if n==0:
            return []
        arr=[-1]*n
        for i in range(n):
            for j in range(1,n):
                idx=(i+j)%n
                if nums[idx]>nums[i]:
                    arr[i]=nums[idx]
                    break
        return arr
        