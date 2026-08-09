class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack=[]
        arr=[]
        s=''
        n=len(word)
        if ch in word:
            index=word.index(ch)
            for i in range(n):
                if word[i]==ch:
                    s+=word[i]
                    while stack:
                        arr.append(stack.pop())
                    break
                else:
                    stack.append(word[i])
            s+=''.join(arr)
            s+=word[index+1:]
            return s
        else:
            return word

        