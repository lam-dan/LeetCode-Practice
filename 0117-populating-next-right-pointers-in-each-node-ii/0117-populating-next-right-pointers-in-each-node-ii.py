"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Populate each node's .next pointer to point to its right neighbor.
        Works for ANY binary tree (not necessarily perfect, unlike LC 116).
        
        Time:  O(N)   – visit each node exactly once
        Space: O(1)   – no extra data structures, just a few pointers
        """
        if not root:
            return None

        # 'curr' will always point to the current node we are processing
        # on the CURRENT level.
        curr = root

        # Outer loop: process one level at a time, until no more nodes
        while curr:
            # Create a dummy node to serve as the "head" of the NEXT level.
            # This dummy is thrown away at the end of each outer iteration.
            dummy = Node(0)
            # 'tail' always points to the *end* of the list we are building
            # for the next level. It starts at dummy and grows as we find children.
            tail = dummy

            # Inner loop: walk across the current level using the .next pointers
            # (which have already been set during previous outer iterations).
            while curr:
                # If current node has a left child, attach it to the next-level list
                if curr.left:
                    tail.next = curr.left  # stitch it in
                    tail = tail.next       # advance tail

                # If current node has a right child, attach it as well
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next

                # Move horizontally to the next node on the same level
                curr = curr.next

            # At this point, the whole next level is stitched together,
            # starting at dummy.next. 
            # Move 'curr' down to the leftmost node of the next level.
            curr = dummy.next

        # Root hasn't changed; return it as required.
        return root