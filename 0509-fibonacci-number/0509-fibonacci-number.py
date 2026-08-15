class Solution:
    def les(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n]!=0:
            return dp[n]
        dp[n]=(self.les(n-1,dp))+(self.les(n-2,dp))
        return dp[n]
    def fib(self, n: int) -> int:
         dp=[0]*(n+1)
         return  self.les(n,dp)
   
       