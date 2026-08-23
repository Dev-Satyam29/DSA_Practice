class Solution:
    def isPalindromic(self, s: str) -> bool:
        s1=''
        for i in s:
            ans=bin(ord(i))[2:].zfill(8)
            s1+=str(ans)
        if s1==s1[::-1]:
            return True
        else:
            return False
        