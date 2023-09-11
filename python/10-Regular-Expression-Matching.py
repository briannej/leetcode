#bottom up 2D dp 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS, lenP = len(s), len(p)
        dp = [[False]*(lenP+1) for i in range(lenS+1)]
        dp[0][0] = True
    
        for j in range(1, lenP+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
    
        for i in range(1, lenS+1):
            for j in range(1, lenP+1):
                #if chars match look top left
                if p[j-1] in {s[i-1], '.'}:
                    dp[i][j] = dp[i-1][j-1]
                #if we have a * char:
                #1. not to use the previous char
                #2. look one col up, if True, it was possible to make the previous chars in s with some number of *
                #so check if it is possible to make the last char with * as well? (therefore the char before * should match the last s char)
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and p[j-2] in {s[i-1], '.'})
    
        return dp[-1][-1]


# BOTTOM-UP Dynamic Programming
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]


# TOP DOWN MEMOIZATION
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                    match and dfs(i + 1, j)
                )  # use *
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
