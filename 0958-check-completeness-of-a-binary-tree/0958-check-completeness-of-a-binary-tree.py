# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        queue = deque([root])
        seen_null = False

        while queue:
            left_flag = False
            right_flag = False

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if seen_null:
                        return False

                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    seen_null = True
        return True

            


