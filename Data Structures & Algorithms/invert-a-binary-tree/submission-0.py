# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTreeRecursive(self, node: Optional[TreeNode]):
        if node:
            left = node.left
            right = node.right
            node.right = left
            node.left = right
            Solution.invertTreeRecursive(self, node.left)
            Solution.invertTreeRecursive(self, node.right)
        else:
            return
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        Solution.invertTreeRecursive(self, root)
        return root

