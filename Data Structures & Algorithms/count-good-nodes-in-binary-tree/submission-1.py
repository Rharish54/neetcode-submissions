# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            #NOTE: There has to be no prev nodes GREATER -- equal is fine
            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, -math.inf)
