# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # use depth firt search on both which would be O(n)
        # use integer and and flag to make sure each one added at same time is the same only change to false if it's integer dont match at end

        pQueue = deque([p])
        qQueue = deque([q])
        qCount = 0
        pCount = 0
        while pQueue and qQueue:
            if len(pQueue) != len(qQueue):
                return False
            
            for i in range(len(pQueue)):
                pNode = pQueue.popleft()
                qNode = qQueue.popleft()
                if not pNode and  not qNode:
                    continue
                elif not pNode and qNode:
                    return False
                elif not qNode and pNode:
                    return False
                else:

                    if pNode.val != qNode.val:
                        return False
                    
                    
                    pQueue.append(pNode.left)
                    qQueue.append(qNode.left)
                    pQueue.append(pNode.right)
                    qQueue.append(qNode.right)


        return True