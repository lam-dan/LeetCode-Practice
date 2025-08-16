"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return
        # Level Orders BFS Traversal using Queue
        # Populate with "#" to signifiy the end of each level
        # SO basically append after the level order traversal
        # Build queue 
        # Append root 
        q = deque([root])
        self.result = []
        while q:
            # Allows for dynamically appending to the queue 
            # even if a subtree is missing a right or left subtree
            level = len(q)
            prev = None

            for _ in range(level):
                node = q.popleft()

                # Link previous node's next to the current Node
                if prev:
                    prev.next = node
                prev = node # point previous to current node

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # Last node in the level points to None
            prev.next = None
        return root




        

