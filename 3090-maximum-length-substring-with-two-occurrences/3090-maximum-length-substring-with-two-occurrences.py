class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        freq=[0]*26
        ans=0
        l=0
        for r in range(n):
            freq[ord(s[r])-ord('a')]+=1
            while freq[ord(s[r])-ord('a')]>2:
                freq[ord(s[l])-ord('a')]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans

        