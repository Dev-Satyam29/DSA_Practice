class Solution:
    def reverseDegree(self, s: str) -> int:
        freq= {chr(i): 27 - (i - 96) for i in range(97, 123)}
        total=0
        for i in range(len(s)):
            product=freq[s[i]]*(i+1)
            total+=product
        return total
        