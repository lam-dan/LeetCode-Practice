# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Initialize the closest value with the root's value.
        # We'll refine this as we traverse.
        closest = root.val

        node = root
        while node:
            # If this node is closer to target than our current best, update it.
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            # Optional tie-breaker (uncomment if you want smaller value on ties):
            elif abs(node.val - target) == abs(closest - target):
                closest = min(closest, node.val)

            # Use BST property to decide the direction:
            # - If target is less, the closer value (if any) must be in the left subtree.
            # - If target is greater or equal, go right.
            if target < node.val:
                node = node.left
            else:
                node = node.right

        return closest

        # Time: O(H) (height of tree; O(log N) on average, O(N) worst if skewed)
        # Space: O(1) (no recursion stack or extra arrays)
                 



