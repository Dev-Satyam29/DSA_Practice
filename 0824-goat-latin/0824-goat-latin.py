class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        arr=sentence.split(" ")
        for i in range(len(arr)):
            if arr[i][0].lower()in"aeiou":
                arr[i]=arr[i]+"ma"
            else:
                arr[i]=arr[i][1:]+arr[i][0]+"ma"
            arr[i]=arr[i]+((i+1)*'a')
        return " ".join(arr)
        
        