class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        ## RC ##
        ## APPROACH : DP ##
        ## INTUITION : THINK LIKE SUBSET SUM PROBLEM (tushor roy DP solution) Leetcode 416. Partition equal subset sum ##
        # but here  1. our target can range from -totalSum to +totalSum
        #           2. and we dont include True directly from above sequence, coz it is not subsequence we are looking for. so here consider if and only if previous value exists
        # [1,1,1,1,1]
        # 3
        # [
        #   [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
        #   [0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0], 
        #   [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 0], 
        #   [0, 1, 0, 4, 0, 6, 0, 4, 0, 1, 0], 
        #   [1, 0, 5, 0, 10, 0, 10, 0, 5, 0, 1]
        # ]

                ## TIME COMPLEXITY : O(N^2) ##
                ## SPACE COMPLEXITY : O(N^2) ##

        totalSum = sum(nums)
        if(S not in range(-1 * totalSum, totalSum + 1) ): return 0
        dp = [ [ 0 for j in range( totalSum*2 + 1 ) ] for i in range(len(nums))]

        ## BASE CASE ## FIRST ROW ##
        dp[0][totalSum + nums[0]] += 1
        dp[0][totalSum - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range( totalSum*2 + 1 ):

                if( j - nums[i] >= 0 and dp[i-1][j-nums[i]] > 0 ):          # left side
                    dp[i][j] += dp[i-1][j-nums[i]]

                if( j + nums[i] <= totalSum*2 and dp[i-1][j+nums[i]] > 0 ): # right side
                    dp[i][j] += dp[i-1][j+nums[i]]

        print(dp)
        return dp[-1][totalSum + S]





class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)
