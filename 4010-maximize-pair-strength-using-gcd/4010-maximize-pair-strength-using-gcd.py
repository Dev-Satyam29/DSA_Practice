class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        l=len(nums)
        max_gcd=0
        for i in range(l-1):
            for j in range(i+1,l):
                g=(nums[i]*nums[j])//math.gcd(nums[i],nums[j])**2
                if g>max_gcd:
                    max_gcd=g
        return max_gcd
                