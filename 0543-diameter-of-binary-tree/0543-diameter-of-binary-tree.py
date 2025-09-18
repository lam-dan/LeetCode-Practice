# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global tracker for the diameter (longest path found so far in the tree)
        self.diameter = 0

        def dfs(node):
            if node is None:
                return 0  # Base case: empty subtree has height 0

            # Recursively compute the height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # The longest path THROUGH this node = left_height + right_height
            # Update the global diameter if this path is longer than any seen so far
            self.diameter = max(self.diameter, left + right)

            # Return height of the current subtree to parent:
            # 1 for the current node + the taller child height
            return 1 + max(left, right)

        # Run DFS from the root to compute both heights and update diameter
        dfs(root)

        # Final result: the maximum diameter found during DFS
        return self.diameter