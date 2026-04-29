# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        # queue if the node that is added is a right child some how mark it can be seen
        
        # if the node is a left child
        # have to check if it has another 


        # if queue is == 1 this mean the last node on right cause were going to queue left to right

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            rightSide = None
            queueLength = len(queue) # how many elements in the level
            
            for i in range(queueLength):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightSide:
                res.append(rightSide.val)
        return res