class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        temp = abs(num)
        while temp != 0:
            curr = temp % 7
            res = str(curr) + res
            temp = temp // 7
        if num < 0:
            return "-" + res
        else:
            return res if res else "0"