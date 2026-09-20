class Solution:
    def reverseDegree(self, s: str) -> int:
        total=0
        for i in range(len(s)):
            n=27-(ord(s[i])-96)
            product=n*(i+1)
            total+=product
        return total
        