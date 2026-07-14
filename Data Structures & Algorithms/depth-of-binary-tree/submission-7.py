# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)] # tuple containing node + depth
        max_depth = 0
        while stack:
            node, curr_depth = stack.pop()
            max_depth = max(max_depth, curr_depth)

            if node.left:
                # note
                stack.append((node.left, curr_depth + 1))
            if node.right:
                stack.append((node.right, curr_depth + 1))
        
        return max_depth


