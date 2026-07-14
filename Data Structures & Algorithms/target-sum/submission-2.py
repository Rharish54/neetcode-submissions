class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # start at 
        # dp[0] == True

        curr = []
        count = 0
        def dfs(i, total):
            nonlocal count
            if total == target and i >= len(nums):
                # print("this is curr: ", curr)
                count += 1
                return
            
            if i >= len(nums):
                return
            #two options: add i or substract i
            # find L and R tree of each choice

            total += nums[i]
            dfs(i + 1, total)
        
            total -= nums[i] * 2
            dfs(i + 1, total)
            # adding then substracting
        
        dfs(0, 0)
        return count
