class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_digit=0
        prod_digit=1
        rev=n
        while rev>0:
            d=rev%10
            sum_digit+=d
            prod_digit*=d
            rev=rev//10
        total=sum_digit+prod_digit
        if n%total==0:
            return True
        else:
            return False
        