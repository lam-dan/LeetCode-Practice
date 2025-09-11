# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS Approach, Post-Order Processing
        # Accumulate counts on the return traversing back up
        # Update maximum on the way back up as well
        self.diameter = 0
        def dfs(node):
            if node is None:
                return 0
            node_left = dfs(node.left)
            node_right = dfs(node.right)
            self.diameter = max(self.diameter, node_left + node_right)
            return 1 + max(node_left, node_right)
        dfs(root)
        return self.diameter

        # Time Complexity O(n) 
        # Space Complexity is O(n)