# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            # Get the maximum gain from the left and right subtree, discard negative gains
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            # Path sum that includes both left and right child and current node
            current_max_path = node.val + left + right
            # Update the global maximum path sum
            self.max_path_sum = max(self.max_path_sum, current_max_path)
            # Return the max gain by continuing with either left or right subtree
            return node.val + max(left, right)
        dfs(root)
        return self.max_path_sum
        
