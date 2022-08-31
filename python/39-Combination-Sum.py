class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results



#class Solution(object):
    #def combinationSum(self, candidates, target):
        #res = []
    
        #def dfs(nums, target, path):
            #if target < 0:
                #return 
            #if target == 0:
                #res.append(path)
                #return 
            #for i in range(len(nums)):
                #dfs(nums[i:], target-nums[i], path+[nums[i]])
        #dfs(candidates, target, [])
        #return res


#class Solution:
    #def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #res = []

        #def dfs(i, cur, total):
            #if total == target:
                #res.append(cur.copy())
                #return
            #if i >= len(candidates) or total > target:
                #return

            #cur.append(candidates[i])
            #dfs(i, cur, total + candidates[i])
            #cur.pop()
            #dfs(i + 1, cur, total)

        #dfs(0, [], 0)
        #return res
