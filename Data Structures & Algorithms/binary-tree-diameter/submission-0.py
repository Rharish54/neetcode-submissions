# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.count = max(self.count, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.count

            # stack = [root]
            # max_count = 0
            # # i need a way of tracking unique paths

            # while stack:
            #     n = stack.pop
            #     if n.left or n.right:
            #         if n.left:
            #             stack.append(n.left)
            #         else:
            #             stack.append(n.right)
            #         count += 1
            #     else:
            #         max_count = max(max_count, count)

            
            

        