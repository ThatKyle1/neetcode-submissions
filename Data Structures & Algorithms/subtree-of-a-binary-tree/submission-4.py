# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def helper(root,sub):
            
            if not root and not sub:
                return True
            elif not root or not sub:
                return False
            elif root.val != sub.val:
                return False
            else:
                return helper(root.left, sub.left) and helper(root.right, sub.right)
        
        if not root:
            return False
        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)