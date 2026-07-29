# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(r1, r2):
            if r1 is None and r2 is None:
                return True
            if r1 is None or r2 is None or r1.val != r2.val:
                return False
            return helper(r1.left, r2.left) and helper(r1.right, r2.right)
            
        visited = []
        if not root or subRoot is None:
            return False
        
        visited.append(root)

        while visited:
            curr = visited.pop()
            if curr.val == subRoot.val and helper(curr, subRoot):
                return True
            if curr.left:
                visited.append(curr.left)
            if curr.right:
                visited.append(curr.right)
        
        return False
