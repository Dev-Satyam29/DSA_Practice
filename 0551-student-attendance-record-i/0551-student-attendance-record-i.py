class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>=2:
            return False
        i=0
        j=0
        while j<len(s):
            if s[j]=='L':
                j+=1
                if j-i>=3:
                    return False
            else:
                j+=1
                i=j
        return True
        