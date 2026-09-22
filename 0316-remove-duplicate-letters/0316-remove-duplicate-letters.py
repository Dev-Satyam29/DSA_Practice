class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq={}
        visit=set()
        stack=[]
        for i in s:
            freq[i]=freq.get(i,0)+1
        for i in s:
            freq[i]-=1
            if i in visit:
                continue
            while stack and stack[-1]>i and freq[stack[-1]]>0:
                visit.remove(stack.pop())
            stack.append(i)
            visit.add(i)
        return "".join(stack)
        