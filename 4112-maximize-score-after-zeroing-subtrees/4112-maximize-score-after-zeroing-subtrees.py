class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        order = [0]
        for u in order:
            for v in children[u]:
                order.append(v)    
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            u = order[i]
            if not children[u]:
                dp[u] = score[u]
                continue
            totalSum = 0
            minChild = float('inf')
            for v in children[u]:
                totalSum += dp[v]
                if dp[v] < minChild:
                    minChild = dp[v]
            if op[u] == 1:
                dp[u] = score[u] + totalSum - minChild
            else:
                dp[u] = score[u] + totalSum - min(0, minChild)
        return dp[0]