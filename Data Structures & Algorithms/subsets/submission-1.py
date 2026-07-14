class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        def dfs(i):
            if i >= len(nums):
                # because subset is modified, append copy
                print("This is what we added!:", sub)
                res.append(sub.copy())
                return
            
            #decision to append nums i !
            sub.append(nums[i])
            print("This is left subtree:", sub)
            dfs(i + 1)

            # decision NOT to include nums[i]
            sub.pop()
            print("This is right subtree:", sub)
            dfs(i + 1)
        
        dfs(0)
        return res


        #dfs search
        #1 -> 2
            # 1 -> 2 ->3
            # 1 -> 2
            # 1->
        # 1 -> 3
        #2 -> 3
            #2 ->
        # 3 ->
