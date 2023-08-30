#bottom up 2D dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for row in range(len(coins)):
            dp[row][0] = 1
        for row in range(len(coins)):
            for col in range(1, amount+1):
                if coins[row] > col:
                    dp[row][col] = dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col] + dp[row][col-coins[row]]
        return dp[-1][-1]

#bottom up 2D dp
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ROWS = len(coins)
        dp = [[0 for i in range(amount+1)] for x in range(ROWS+1)]
        for i in range(ROWS+1):
            dp[i][0] = 1
        for i in range(1, ROWS+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[ROWS][amount]
#if we wanted to add a first row of 0s, then row-1 would corespond to coins index
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        M = [[0 for i in range(amount+1)] for x in range(n+1)]
        for i in range(n+1):
            M[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    M[i][j] = M[i-1][j]
                else:
                    M[i][j] = M[i-1][j] + M[i][j-coins[i-1]]
        return M[n][amount]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]