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
                return True, 0
            
            balenced_l, l = recurse(root.left)
            balenced_r, r = recurse(root.right)

            balenced = (abs(l-r) <= 1 and balenced_r and balenced_l)
                
            return balenced, 1 + max(l, r)
        
        balenced, _ = recurse(root)
        return balenced
