# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        goodNodes = 1
        maxNumber = root.val
        def dfs(root, prevMaxNumber):
            if not root:
                return 0
            
            if root.val >= prevMaxNumber:
                prevMaxNumber = root.val
                return 1 + dfs(root.left, prevMaxNumber) + dfs(root.right,prevMaxNumber)
            else:
                return dfs(root.left, prevMaxNumber) + dfs(root.right,prevMaxNumber)


        return 1 + dfs(root.left, maxNumber) + dfs(root.right, maxNumber)