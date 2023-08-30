class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        first,second=0,0
        for i in range(len(nums)):
            first,second=second, max(first+nums[i],second)
        return second        

