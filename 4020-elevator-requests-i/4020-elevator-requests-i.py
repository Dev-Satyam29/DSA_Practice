class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        total=0
        requests.insert(0,0)
        for i in range(1,len(requests)):
            dis=abs(requests[i-1]-requests[i])
            total+=dis
        return total
        