# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # We need to track 3 things
        # left subtree depth
        # right subtree depth
        # maximum diameter
        self.max_diameter = 0

        def dfs(node):
            if node is None:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # Update global max diameter
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            # Plus 1 is to count the current node on the return
            # max is to converge the counts at each root of the subtree
            return 1 + max(left_depth, right_depth)
        dfs(root)
        return self.max_diameter