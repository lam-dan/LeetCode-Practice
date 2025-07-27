# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level-order traversal (Breadth-First Search) of a binary tree.
        Returns a list of levels, where each level is a list of node values.

        Time Complexity: O(n), where n is the number of nodes (each node is visited once)
        Space Complexity: O(n), due to the queue and result list
        """

        # Step 1: Handle the empty tree case
        if not root:
            return []  # No nodes to process, return an empty list

        # Step 2: Initialize a queue for BFS and a list for the final result
        queue = deque([root])  # Start with the root node in the queue
        result = []            # This will store level-by-level node values

        # Step 3: Process the queue until it's empty
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level = []               # Temporary list to store this level's values

            # Step 4: Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()        # Dequeue the front node from the queue
                level.append(node.val)        # Add its value to the current level list

                # Step 5: Enqueue the node's children (if they exist)
                if node.left:
                    queue.append(node.left)   # Add left child to the queue
                if node.right:
                    queue.append(node.right)  # Add right child to the queue

            # Step 6: After processing all nodes at this level, add the level list to result
            result.append(level)

        # Step 7: Return the list of levels
        return result
            
            




            

            




        
