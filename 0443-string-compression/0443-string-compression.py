class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        i=0
        ans=0
        while i<len(chars):
            letter=chars[i]
            count=0
            while i<len(chars) and chars[i]==letter:
                count+=1
                i+=1
            chars[ans]=letter
            ans+=1
            if count>1:
                s=str(count)
                for c in s :
                    chars[ans]=c
                    ans+=1
        return ans

                
        