# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val

        node = root
        while node:
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
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
        
                 



