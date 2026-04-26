# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # pre order will tell us what node in list is the root node
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # index of inorder which  will give us the split of whats in left and right tree

        root.left = self.buildTree(preorder[1: mid + 1],inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])

        return root