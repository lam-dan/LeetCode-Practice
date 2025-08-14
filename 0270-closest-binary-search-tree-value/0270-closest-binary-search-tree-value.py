# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        node = root
        closest = node.val


        while node:
            # Preprocessing
            current_delta = abs(node.val - target)
            closest_delta = abs(closest - target)

            if current_delta < closest_delta:
                closest = node.val
            elif current_delta == closest_delta:
                closest = min(closest, node.val) # Handle edge cases where nodes are equal

            # Traversal aftrerwards
            if node.val < target:
                node = node.right
            else:
                node = node.left
        return closest

        # Time Complexity is O(n) 
        # Space Complexity is O(1) not creating an extra spaace
            

            

