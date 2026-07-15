class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #recursive dfs

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        
        if dfs(root) != -1:
            return True
        else:
            return False