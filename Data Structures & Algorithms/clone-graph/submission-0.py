"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:        
        if not node:
            return node
        
        index_to_node = {}
        root = Node(val=node.val)
        index_to_node[root.val] = root
        queue = deque([(root, node)])
        while queue:
            new_node, old_node = queue.popleft()
            for n in old_node.neighbors:
                if index_to_node.get(n.val):
                    new_node.neighbors.append(index_to_node[n.val])
                else:
                    new_neighbor = Node(val=n.val)
                    index_to_node[new_neighbor.val] = new_neighbor
                    new_node.neighbors.append(new_neighbor)                    
                    queue.append((new_neighbor, n))

        return root
