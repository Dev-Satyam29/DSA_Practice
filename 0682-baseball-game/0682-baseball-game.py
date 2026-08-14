class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        n=len(operations)
        for i in operations:
            if i.isdigit() or (i[0]=="-" and i[1:].isdigit()):
                stack.append(int(i))
            elif i=='C':
                stack.pop()
            elif i=='D':
                res=int(stack[-1])*2
                stack.append(res)
            elif i=='+':
                resi=stack[-1]+stack[-2]
                stack.append(resi)
        return sum(stack)