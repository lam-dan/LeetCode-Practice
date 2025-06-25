# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(root, total):
            if root is None:
                return 0
            total = total * 10 + root.val

            if root.left is None and root.right is None:
                return total

            left = dfs(root.left, total)
            right = dfs(root.right, total)
            return left + right

        return dfs(root, 0)