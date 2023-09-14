class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        first,second=0,0
        for i in range(len(nums)):
            first,second=second, max(first+nums[i],second)
        return second        

#recursive top down with memo
class Solution:
    def rob(self, nums: List[int]) -> int:
        hashmap={}

        def helper(n, nums):
            if len(nums)==0:
                return 0            
            if n not in hashmap:
                if n==0:
                    hashmap[0]=nums[0]
                elif n==1:
                    hashmap[1]=max(nums[0],nums[1])
                else:
                    hashmap[n]=max(helper(n-1,nums), helper(n-2,nums)+nums[n])

            return hashmap[n]


        a=helper(len(nums)-2,nums[0:-1])
        hashmap={}
        b=helper(len(nums)-2,nums[1:])

        return max(nums[0],a,b)