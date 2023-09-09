#2D Dynamic programing- start from row 0 coloum 0
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ROWS=len(s2)
        COLS=len(s1)
        if len(s3) != ROWS+COLS:return False
        dp=[[False for _ in range(COLS+1)] for _ in range(ROWS+1)]
        dp[0][0]=True                  
        for row in range(ROWS+1):
            for col in range(COLS+1):
                if col>0 and s3[row+col-1]==s1[col-1]:
                    if dp[row][col-1]:
                        dp[row][col]= True        
                    
                if row>0 and s3[row+col-1]==s2[row-1]:
                    if dp[row-1][col]:
                        dp[row][col]= True
                     
        return dp[-1][-1]
        
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ROWS=len(s2)
        COLS=len(s1)
        if len(s3) != ROWS+COLS:return False
        dp=[[False for _ in range(COLS+1)] for _ in range(ROWS+1)]
        dp[0][0]=True
    
        for row in range(1,ROWS+1):
            if s3[row-1]==s2[row-1]:
                if dp[row-1][0]:
                    dp[row][0]= True    
        for col in range(1,COLS+1):
            if s3[col-1]==s1[col-1]:
                if dp[0][col-1]:
                    dp[0][col]= True

                        
        for row in range(1,ROWS+1):
            for col in range(1,COLS+1):
                if s3[row+col-1]==s1[col-1]:
                    if dp[row][col-1]:
                        dp[row][col]= True        
                    
                if s3[row+col-1]==s2[row-1]:
                    if dp[row-1][col]:
                        dp[row][col]= True
                     
        return dp[-1][-1]




class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]
