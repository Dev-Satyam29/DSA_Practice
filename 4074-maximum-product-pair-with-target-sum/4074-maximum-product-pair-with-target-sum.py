class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        res=[-1]*2
        max_product=float('-inf')
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]==target and nums[i]!=nums[j]:
                    if nums[i]*nums[j]>max_product:
                        max_product=nums[i]*nums[j]
                        if nums[i]>nums[j]:
                            res[0]=i
                            res[1]=j
                        else:
                            res[0]=j
                            res[1]=i
                        
        return res
        