# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        res = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            if left_to_right == False:
                level.reverse()
            
            res.append(level)
            # toggle the direction
            if left_to_right == True:
                left_to_right = False
            else:
                left_to_right = True

        return res


