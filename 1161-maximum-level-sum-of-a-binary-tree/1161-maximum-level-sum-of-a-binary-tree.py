# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        # Handle Starting Level Value
        max_level = float('-inf')
        ans = 0
        level = 0

        while queue:
            level += 1
            level_total = 0

            # Iterate over all nodes at each level
            for _ in range(len(queue)):
                node = queue.popleft()
                level_total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Post Processing
            if level_total > max_level:
                max_level = level_total
                ans = level

        return ans
            



            
            
