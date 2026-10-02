class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        i=0
        count=1
        max_count=1
        for j in range(1,len(nums)):
            if nums[j]<=nums[i]:
                i+=1
                count=1
            else:
                count+=1
                i+=1
            max_count=max(count,max_count)
        return max_count
        