#bottom up dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[m - 1][n - 1]




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
