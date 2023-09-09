#bottom up 2D dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0] *(n+1) for _ in range(m+1)]
        dp[1][0]=1
        for row in range(1,m+1):
            for col in range(1,n+1):
                dp[row][col]=dp[row-1][col]+dp[row][col-1]
        print(dp)
        return dp[-1][-1]


#bottom up 2D dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[m - 1][n - 1]

#bottom up 1D dynamic programming- memory optimization with one row one variable
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[0]*(n)
        dp[0]=1
        for _ in range(m):
            prev=0
            for col in range(n):
                dp[col]+=prev
                prev=dp[col]
        return dp[-1]

#bottom up 1D dynamic programming- memory optimization with 2 rows
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        aboveRow = [1] * n

        for _ in range(m - 1):
            currentRow = [1] * n
            for i in range(1, n):
                currentRow[i] = currentRow[i-1] + aboveRow[i]
            aboveRow = currentRow

        return aboveRow[-1]
    
    
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)
