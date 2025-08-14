# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            if node.left is None:
                return 1 + dfs(node.right)
            if node.right is None:
                return 1 + dfs(node.left)
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + min(left, right)

        return dfs(root)