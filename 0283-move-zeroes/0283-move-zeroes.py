class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        l=0
        r=1
        while r<n:
            if nums[l]!=0:
                l+=1
                if l>=r:
                    r=l+1
            elif nums[r]==0:
                r+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
        return nums