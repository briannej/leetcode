class Solution:
    def rob(self, nums: List[int]) -> int:
        first,second=0,0
        for i in range(len(nums)):
            first,second=second, max(first+nums[i],second)
        return second


class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap={-1:0,-2:0}
        def helper(n):
            if n not in hashmap:
                hashmap[n]=max(nums[n]+helper(n-2), helper(n-1))
            return hashmap[n]
        return helper(len(nums)-1)

#recursive with memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap={}
        def helper(n):
            if n not in hashmap:
                if n==0:
                    hashmap[0]=nums[0]
                elif n==1:
                    hashmap[1]=max(nums[0],nums[1])
                else:
                    hashmap[n]=max(helper(n-1), helper(n-2)+nums[n])

            return hashmap[n]

        return helper(len(nums)-1) 


class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge cases:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums)
        
        # dynamic programming - decide each problem by its sub-problems:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        return dp[-1]




class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
