class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero=0
        one=0
        ans=0
        for i in s:
            if i=="0":
                zero+=1
            if i=="1":
                one+=1
            if abs(zero-one)<=1:
                ans+=1
        return ans
        