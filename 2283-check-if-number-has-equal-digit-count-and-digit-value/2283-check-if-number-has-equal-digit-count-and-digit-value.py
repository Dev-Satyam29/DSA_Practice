class Solution:
    def digitCount(self, num: str) -> bool:
        freq={}
        for i in num:
            freq[i]=freq.get(i,0)+1
        for i in range(len(num)):
            if int(num[i])!=freq.get(str(i),0):
                return False
        return True


        