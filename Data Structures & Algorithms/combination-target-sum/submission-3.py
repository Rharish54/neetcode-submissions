class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # hold all unique subsets == target
        res = []

        def dfs(idx, subset, tracker):
        # idx = curr index, subset. , tracker = total sum so far
            if tracker == target:
                res.append(subset.copy())
                return
            
            if tracker > target or idx >= len(nums):
                return
            
            subset.append(nums[idx])
            dfs(idx, subset, tracker + nums[idx])

            subset.pop()
            dfs(idx + 1, subset, tracker)

        dfs(0, [], 0)
        return res