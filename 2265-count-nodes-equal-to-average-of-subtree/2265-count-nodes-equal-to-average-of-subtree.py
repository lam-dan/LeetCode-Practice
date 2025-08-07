# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.global_count = 0
        # why don't we need to pass in total sum and total count in dfs()
        # That would be true if we were trying to maintain a running total 
        # across recursive calls (e.g. pre-order logic).
        # we're doing post-order, and the sum/count bubble up from child to parent.
        # If you tried pre-order logic, you wouldn't get an accurate calculation of total sum, total acount
        # since you're too early in the traversal to calculate for the subtree average
        def dfs(node):
            # Base Case
            if node is None:
                return (0, 0)

            (left_sum, left_count) = dfs(node.left)
            (right_sum, right_count) = dfs(node.right)
            
            # Calculate add left and right subtree total sum when merging
            total_sum = left_sum + right_sum
            total_sum += node.val # Add current node val

            # Calculate left and right subtree counts
            total_count = left_count + right_count
            total_count += 1 # Add current node count

            avg = total_sum // total_count # Calculate average for current node

            if avg == node.val: # Compare current average for node vs current node val
                self.global_count += 1

            return (total_sum, total_count) # This is the return for the running total from child to parent

        dfs(root)
        return self.global_count

        # Time Complexity is O(n) since we need to traverse to all the nodes in the tree to calculate all the average
        # at each subtree node

        # Space Complexity is O(1) since we don't create any additional space
    
        