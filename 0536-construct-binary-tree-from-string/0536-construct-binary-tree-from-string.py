# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        # Recursive dfs level order traversal for serialization
        # This is only deserialization
        
        return self._str2treeInternal(s,0)[0]


    def _getNumber(self, s, index):
        is_negative = False

        # Check if the number starts with "-"
        if s[index] == "-":
            is_negative = True
            index += 1
        
        number = 0
        # Parse consecutive digits into an integer
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1
        
        # Apply sign if needed
        return number if not is_negative else -number, index


    
    def _str2treeInternal(self, s, index):
        if index == len(s):
            return None, index
        
        # 1) Parse the root node's value
        value, index = self._getNumber(s, index)
        node = TreeNode(value)

        # 2) Parse the left child if the next character is "("
        if index < len(s) and s[index] == "(":
            node.left, index = self._str2treeInternal(s, index + 1)

        # 3) Parse the right child if the left exists and the next char is "("
        if node.left and index < len(s) and s[index] == "(":
            # Skip "(" and parse the right subtree
            node.right, index = self._str2treeInternal(s, index + 1)
        
        # 4) If current char is ")", skip it (end of this subtree)
        if index < len(s) and s[index] == ")":
            index += 1
        
        return node, index

        # Time Complexity is O(n) where n is the number of characters in the string
        # Space Complexity is O(h) where h is the height of the tree because each recursive call creates space in memory for the call stack.
        

