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
        self.max_level = float('-inf')
        self.ans = 0
        self.level = 0

        while queue:
            self.level += 1
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
            if level_total > self.max_level:
                self.max_level = level_total
                self.ans = self.level

        return self.ans
            



            
            
