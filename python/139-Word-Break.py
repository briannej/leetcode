#bottom up dynamic programming - with dp padding
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for word in wordDict:
                if i-len(word)>=0 and s[i-len(word):i]==word and dp[i-len(word)]:
                    dp[i]=True
                    break   
        return dp[-1]

#bottom up dynamic programming - with no dp padding
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                # Handle out of bounds case
                if i < len(word) - 1:
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break

        return dp[-1]



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
