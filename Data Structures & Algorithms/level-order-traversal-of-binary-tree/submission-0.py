from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_array = []
        if not root:
            return return_array
        
        queue = deque()
        queue.append((root,1))

        while queue:
            root, level = queue.popleft()            
            if root:
                if len(return_array) < level:
                    return_array.append([])
                return_array[level-1].append(root.val)

                if root.left:
                    queue.append((root.left,level+1))
                if root.right:
                    queue.append((root.right,level+1))
        
        return return_array

