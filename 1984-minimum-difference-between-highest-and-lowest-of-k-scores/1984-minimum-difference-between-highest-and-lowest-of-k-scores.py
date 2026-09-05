class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==1:
            return 0
        nums.sort()
        min_sum=nums[k-1]-nums[0]
        i=1
        j=i+k-1
        while j<n:
            temp=nums[j]-nums[i]
            min_sum=min(min_sum,temp)
            i+=1
            j+=1
        return min_sum
        