# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # Edge case: An empty tree is not considered complete by this implementation.
        if root is None:
            return False

        # Initialize the queue with the root for level-order traversal (BFS)
        queue = deque([root])

        # Flag to mark if we've seen a missing child (i.e., a gap in the tree)
        # Once a missing child is seen, all following nodes must be leaf nodes
        seen_null = False

        while queue:
            # Iterate through all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()

                # Check left child
                if node.left:
                    if seen_null:
                        # If we've already seen a missing child and now encounter a non-null child,
                        # the tree is not complete (a gap was filled improperly)
                        return False
                    queue.append(node.left)
                else:
                    # Mark that a null (missing) child was encountered
                    seen_null = True

                # Check right child
                if node.right:
                    if seen_null:
                        # Same logic applies: a right child after a null indicates invalid structure
                        return False
                    queue.append(node.right)
                else:
                    seen_null = True

        # If the loop completes without returning False, the tree is complete
        return True
            


