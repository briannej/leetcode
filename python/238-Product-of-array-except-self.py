class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1] * len(nums)
        for i in range(len(nums)-1):
            output[i+1] = nums[i] * output[i]
        mult =1
        for j in reversed(range(len(nums)-1)):
            mult *= nums[j+1]
            output[j] *= mult
        return output