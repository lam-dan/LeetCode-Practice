# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Edge case where the delta is basically tied and we need to 
        # take the smallest node value
        # Regular Binary Tree Traversing without recursion
        # Pre Order processing
        node = root
        closest = node.val

        while node:
            current_delta = abs(node.val - target)
            closest_delta = abs(closest - target)

            if current_delta < closest_delta:
                closest = node.val
            # Edge case where the delta is tied
            elif current_delta == closest_delta:
                closest = min(closest, node.val)
                
            if node.val < target:
                node = node.right
            else:
                node = node.left


        return closest
            



