# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.total_count = 0
        # Need to keep track of current node, and total count
        # Calculate average at each node
        # Average is calculated by the sum of the left subtree, right subtree
        # current node, and total count
        def dfs(node):
            # Base Case for nodes that are null
            if node is None:
                return (0,0)

            # Do I need to check for existence - no
            # Traversal is needed for every node
            left_count, left_total = dfs(node.left)
            right_count, right_total = dfs(node.right)

            # Calculating Total Count + Current Node
            total_count = left_count + right_count
            total_count += 1

            # Calculating Total Value
            total_value = left_total + right_total
            total_value += node.val

            # Calculating Average
            avg = total_value // total_count

            if avg == node.val:
                self.total_count += 1

            return total_count, total_value # This will return to line 21 or 22

        dfs(root)
        return self.total_count
        