class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        mid=n//2
        a=s[:mid]
        b=s[mid:]
        count1=0
        count2=0
        vow='aeiouAEIOU'
        for i in a:
            if i in vow:
                count1+=1
        for i in b:
            if i in vow:
                count2+=1
        if count1==count2:
            return True
        else:
            return False
        