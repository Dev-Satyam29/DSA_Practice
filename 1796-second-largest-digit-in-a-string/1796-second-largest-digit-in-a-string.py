class Solution:
    def secondHighest(self, s: str) -> int:
        first=float('-inf')
        second=float('-inf')
        for i in s:
            if i.isdigit():
                if int(i)>first:
                    second=first
                    first=int(i)
                elif int(i)>second and int(i)<first:
                    second=int(i)
        if second==float('-inf'):
            return -1
        else:
            return second