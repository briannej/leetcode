#also next solution is good. this one initializes row 0 and col 0 in the same loop. next one has separate loops
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        COLS=len(word1)
        ROWS=len(word2)
        
        dp=[[0]*(COLS+1) for _ in range(ROWS+1)]
        
        for row in range(ROWS+1):
            for col in range(COLS+1):
                if row==0 and col==0:
                    continue
                if row==0:
                    dp[row][col]=1+ dp[row][col-1]
                elif col==0:
                    dp[row][col]=1+ dp[row-1][col]    

                else:
                    if word1[col-1]== word2[row-1]:
                        dp[row][col]=dp[row-1][col-1]
                    else:
                        dp[row][col]=1+ min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])
        return dp[-1][-1]


#bottom up 2D dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # dp[i][j] := min # Of operations to convert word1[0..i) to word2[0..j)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i

        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[m][n]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]
