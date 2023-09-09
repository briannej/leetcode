#bottom up 2D dynamic programming
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS=len(text1)
        COLS=len(text2)
        dp=[[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        for row in range(1, ROWS+1):
            for col in range(1,COLS+1):
                if text2[col-1]==text1[row-1]:
                    dp[row][col]=1+dp[row-1][col-1]
                else:
                    dp[row][col]=max(dp[row-1][col],dp[row][col-1])
        return dp[-1][-1]

#bottom up 1D dynamic programming- memory optimization with two rows
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1,text2=text2,text1
        ROWS=len(text1)
        COLS=len(text2)
        above=[0 for _ in range(COLS+1)]
        for row in range(1,ROWS+1):
            current=[0]* (COLS+1)
            for col in range(1,COLS+1):
                if text2[col-1]==text1[row-1]:
                    current[col]=1+above[col-1]
                else:
                    current[col]=max(above[col],current[col-1])
                
            above=current
        return current[-1]

#bottom up 1D dynamic programming- memory optimization with two rows- minor time optimization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1,text2=text2,text1
        ROWS=len(text1)
        COLS=len(text2)
        above=[0 for _ in range(COLS+1)]
        current=[0]* (COLS+1)
        for row in range(1,ROWS+1):
            for col in range(1,COLS+1):
                if text2[col-1]==text1[row-1]:
                    current[col]=1+above[col-1]
                else:
                    current[col]=max(above[col],current[col-1])

            current,above=above,current
        return above[-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
