class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        row=len(accounts)
        col=len(accounts[0])
        wealth=0
        for i in range(row):
            total=0
            for j in range(col):
                total+=accounts[i][j]
            wealth=max(wealth,total)
        return wealth
        