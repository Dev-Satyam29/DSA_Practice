class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first={0:-1}
        bal=0
        ans=0
        for i,num in enumerate(nums):
            if num==1:
                bal+=1
            else:
                bal-=1
            if bal in first:
                ans=max(ans,i-first[bal])
            else:
                first[bal]=i
        return ans
        