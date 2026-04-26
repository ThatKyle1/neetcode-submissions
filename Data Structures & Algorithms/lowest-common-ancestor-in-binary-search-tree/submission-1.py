# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # cases to look at
        # if curr node is < p and q
        # look at left tree
        # vice versa
        # on other case if it's curr val is between p and q
        # return curr node val
        # if hit a node p or q then that is the LCA

        #queue = deque([root])


        rightBound = max(p.val, q.val)
        leftBound = min(p.val, q.val)
        '''
        while queue:
            node = queue.popleft()
            
            
            if node.val >= leftBound and node.val <= rightBound:
                return node
            if node.val > rightBound:
                queue.append(node.left)
            else:
                queue.append(node.right)
        '''
        curr = root
        while curr:
            if curr.val > leftBound and curr.val > rightBound:
                curr = curr.left
            elif curr.val < leftBound and curr.val < rightBound:
                curr = curr.right
            else:
                return curr
