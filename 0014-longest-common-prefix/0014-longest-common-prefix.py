class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        res=''
        left=strs[0]
        right=strs[-1]
        i=0
        while i<len(left) and i<len(right):
            if left[i]==right[i]:
                res+=left[i]
                i+=1
            else:
                break
        return res
        