"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # make a visited because undirected graph
        # we want to also create new node everytime we reach a node not in visited 

        if not node:
            return None
        newNodes = {}

        queue = deque()
        queue.append(node)
        newNodes[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in newNodes:
                    newNodes[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                newNodes[curr].neighbors.append(newNodes[neighbor])
        
        return newNodes[node]