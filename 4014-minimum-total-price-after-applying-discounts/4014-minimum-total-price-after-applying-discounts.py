class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        result=0
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        n=len(prices)
        l=len(discounts)
        left,right=0,0
        while left<n and right<l:
            d=(prices[left]*(100-discounts[right]))/100
            result+=d
            left+=1
            right+=1
        while left<n:
            result+=prices[left]
            left+=1
        return result


        