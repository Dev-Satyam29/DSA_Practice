class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        freq={}
        n=len(keysPressed)
        freq[keysPressed[0]]=releaseTimes[0]
        for i in range(1,n):
            if keysPressed[i] not in freq:
                freq[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
            if keysPressed[i] in freq:
                if freq[keysPressed[i]]>releaseTimes[i]-releaseTimes[i-1]:
                    pass
                else:
                    freq[keysPressed[i]]=releaseTimes[i]-releaseTimes[i-1]
        sorted_val = sorted(freq.keys(), key=lambda k: (freq[k], k), reverse=True)
        first_key = next(iter(sorted_val))
        return first_key
            
        