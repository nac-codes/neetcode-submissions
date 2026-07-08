# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    global_max = 0

    def findMax(self, root: Optional[TreeNode]):
        if not root:
            return 0

        l = self.findMax(root.left)
        r = self.findMax(root.right)

        if l + r > self.global_max:
            self.global_max = l + r
        
        return 1 + max(l, r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.findMax(root)

        return_max = self.global_max
        self.global_max = 0

        return return_max
        
        