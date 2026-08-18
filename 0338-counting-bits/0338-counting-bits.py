class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        def count_ones(n):
            count = 0
            while n > 0:
                n = n & (n - 1) 
                count += 1       
            return count
        i=0
        while i<=n:
            dp[i]=count_ones(i)
            i+=1
        return dp


        