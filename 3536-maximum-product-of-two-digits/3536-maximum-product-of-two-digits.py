class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        while n>0:
            s=n%10
            arr.append(s)
            n=n//10
        arr.sort(reverse=True)
        return arr[0]*arr[1]
       