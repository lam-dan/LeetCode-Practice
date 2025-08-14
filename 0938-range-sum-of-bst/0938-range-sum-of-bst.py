# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # DFS Pre-Order Traversal
        self.sum = 0

        def dfs(node):
            if node is None:
                return 0
            if low <= node.val <= high:
                self.sum += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.sum

        # Time Complexity is O(n)
        # Space Complexity is O(n)