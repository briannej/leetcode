class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            #[5]
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[r] >= nums[m]:
                if nums[m]< target and target <= nums[r]:
                    l=m+1
                else:
                    r=m-1
            elif nums[l] <= nums[m]:
                if nums[m] > target and target >=nums[l]:
                    r=m-1
                else:
                    l=m+1
                
        return -1
            
