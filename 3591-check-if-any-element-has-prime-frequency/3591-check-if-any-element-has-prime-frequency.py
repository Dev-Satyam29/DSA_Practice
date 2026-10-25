class Solution:
    def isPrime(self,n):
        if n<2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for k,v in freq.items():
            if self.isPrime(v):
                return True
        return False

        