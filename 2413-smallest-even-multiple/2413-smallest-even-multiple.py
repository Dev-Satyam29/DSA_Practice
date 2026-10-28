class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        found=False
        i=n
        while found!=True:
            if i%2==0 and i%n==0:
                return i
                found=True
                break
            else:
                i+=1

        