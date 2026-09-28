class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        ans=0
        for i in s:
            if i==")":
                depth-=1
            if i!="(":
                continue
            depth+=1
            if depth>ans:
                ans=depth
        return ans
        