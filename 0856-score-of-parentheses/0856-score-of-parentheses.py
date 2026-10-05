class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                temp=stack.pop()
                if temp==0:
                    temp=1
                else:
                    temp=2*temp
                stack[-1]+=temp
        return stack[-1]
        