class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        row=len(nums)
        res=0
        for i in range(row):
            if isprime(nums[i][i]):
                res=max(nums[i][i],res)
            if isprime(nums[i][row-i-1]):
                res=max(nums[i][row-i-1],res)
        return res

