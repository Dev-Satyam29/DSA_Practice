class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        freq={}
        for k,v in knowledge:
            freq[k]=v
        s1=""
        i=0
        while i<len(s):
            if s[i]=="(":
                j=i+1
                while s[j]!=")":
                    j+=1
                key=s[i+1:j]
                if key in freq:
                    s1+=freq[key]
                else:
                    s1+='?'
                i=j+1
            else:
                s1+=s[i]
                i+=1
        return s1
        