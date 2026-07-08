# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 0

    def delve(self, root: Optional[TreeNode], depth: int):
        if not root:
            if depth > self.max_depth:
                self.max_depth = depth
            return
        
        self.delve(root.left, depth+1)
        self.delve(root.right, depth+1)
                

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.delve(root, 0)

        return self.max_depth