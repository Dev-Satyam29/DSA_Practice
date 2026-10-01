class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapp={')':'(','}':"{","]":'['}
        for ch in s:
            if ch in mapp:
                if not stack or stack[-1]!=mapp[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)==0
        