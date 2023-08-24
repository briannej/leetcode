#buttomup dp
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first,second=0,0
        for i in range(2,len(cost)+1):
            first, second=second,min(first+cost[i-2],second+cost[i-1])
        return second
#recursive top down with memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hashmap={0:0,1:0}
        def helper(n):
            if n not in hashmap:
                hashmap[n]= min(helper(n-2)+cost[n-2], helper(n-1)+cost[n-1])
            return hashmap[n]
        return helper(len(cost))

#recursive with lru-cache
from functools import lru_cache
class Solution:    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we cannot pass a list to function with lru_cache, so a helper function is used
        @lru_cache
        def helper(n):
            if n==0 or n==1:
                return 0
            return min(helper(n-2)+cost[n-2], helper(n-1)+cost[n-1])
        return helper(len(cost))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
