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
        ROWS= len(nums)
        if(S not in range(-1 * totalSum, totalSum + 1) ): return 0
        dp= [[0]*(totalSum*2+1) for _ in range(ROWS+1)]
        dp[0][totalSum]=1

        
        for row in range(1,ROWS+1):
            for col in range(totalSum*2 + 1):
                if col - nums[row-1] >= 0:  # left side
                    dp[row][col] += dp[row-1][col-nums[row-1]]
                if col + nums[row-1] <= totalSum*2:  # right side
                    dp[row][col] += dp[row-1][col+nums[row-1]]
                
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
