# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val            # Value of the node
        self.left = left          # Left child node
        self.right = right        # Right child node

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []           # Stack to simulate the in-order traversal
        self.push_all(root)       # Initialize the stack with the leftmost path from root

    def push_all(self, node: Optional[TreeNode]):
        if node is None:
            return 
        # Push all left children of the node onto the stack
        while node:
            self.stack.append(node)  # Add current node to stack
            node = node.left         # Move to the left child

    def next(self) -> int:
        # Return the next smallest value in the BST
        node = self.stack.pop()      # Pop the top node (next in in-order)
        self.push_all(node.right)   # Push the left path of the right child, if any
        return node.val            # Return the value of the current node

    def hasNext(self) -> bool:
        # Return True if there are more nodes to visit
        return len(self.stack) > 0  # Stack is non-empty if there are remaining nodes

    # Time Complexity:
    # - The `push_all(node)` method walks down the leftmost path of the given node,
    #   pushing each node onto the stack. In the worst case, this is O(h) per call,
    #   where h is the height of the tree or subtree.
    # - However, each node in the entire tree is pushed and popped exactly once during
    #   the full iteration, meaning the total cost across all calls to `push_all` is O(n),
    #   where n is the number of nodes in the tree.
    # - Therefore:
    #     * `__init__`: O(h) for the initial `push_all(root)`
    #     * `next()`: amortized O(1), total O(n) across all calls
    #     * `hasNext()`: O(1)

    # Space Complexity:
    # - O(h), where h is the height of the tree.
    # - This is the maximum size of the stack at any point, as it only stores the
    #   current path of nodes (left spine) leading to the next smallest element.
    # - In a balanced BST, this is O(log n); in the worst case (completely skewed),
    #   this is O(n).




        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()