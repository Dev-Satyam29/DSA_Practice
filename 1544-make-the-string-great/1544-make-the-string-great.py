class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        alph = {chr(i): chr(i + 32) for i in range(65, 91)}
        for ch in s:
            if stack:
                if  ch in alph and stack[-1]==alph[ch]:
                    stack.pop()
                    continue
                if stack[-1] in alph and alph[stack[-1]]==ch:
                    stack.pop()
                    continue
            
            stack.append(ch)
        return "".join(stack)