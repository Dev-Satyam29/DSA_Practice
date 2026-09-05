class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        temp_sum=sum(nums[:k])
        max_sum=temp_sum
        i=0
        j=k
        while j<n:
            temp_sum=temp_sum-nums[i]+nums[j]
            max_sum=max(temp_sum,max_sum)
            i+=1
            j+=1
        return max_sum/k
        