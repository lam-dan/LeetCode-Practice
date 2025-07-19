"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None  # If the original list is empty, return None immediately

        tmp = head
        # First pass: duplicate each node and insert it right after the original node
        while tmp:
            copyNode = Node(tmp.val)  # Create copied node
            copyNode.next = tmp.next  # Link new node to next
            tmp.next = copyNode       # Insert copy right after the original node
            tmp = copyNode.next       # Move to the next original node

        tmp = head
        # Second pass: assign random pointers to the copied nodes
        while tmp:
            copyNode = tmp.next
            if tmp.random:
                # The copy's random should point to the copy of tmp.random
                copyNode.random = tmp.random.next
            tmp = tmp.next.next  # Move to the next original node

        # Third pass: separate the interleaved list into original and copied lists
        dummy = Node(-1)
        res = dummy
        tmp = head

        while tmp:
            copyNode = tmp.next
            res.next = copyNode      # Append copied node to result list
            tmp.next = copyNode.next # Restore the original list
            tmp = tmp.next           # Move to next original node
            res = res.next           # Move in copied list

        return dummy.next

        # O(n) time complexity where n is the number of nodes in the linked list
        # O(1) space complexity since we don't create extra space  


        


            



        

        