# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(root: Optional[TreeNode]):
            if not root:
                return 0
            
            l = recurse(root.left)
            r = recurse(root.right)

            if abs(l-r) > 1:
                return -100000000

            return 1 + max(l, r)
        
        return False if recurse(root) <= -1 else True
