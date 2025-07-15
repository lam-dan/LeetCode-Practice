# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if current node is None, or matches p or q
        if root is None:
            return None
        if root == p or root == q:
            return root
        
        
        # Recurse on left and right subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a non-null result, current root is the LCA
        if left and right:
            return root

        # If only one side is non-null, return that result
        if left:
            return left
        else:
            return right