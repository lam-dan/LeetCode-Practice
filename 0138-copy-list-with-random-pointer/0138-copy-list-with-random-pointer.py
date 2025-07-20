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
            return None  # Edge case: If the original list is empty, return None

        curr = head
        # === First pass: clone each node and insert it right after the original node ===
        while curr:
            # Create a new node (copy) with the same value
            copyNode = Node(curr.val)
            # Insert the copy node right after the original node
            copyNode.next = curr.next
            curr.next = copyNode
            # Move tmp to the next original node (skip the copy we just inserted)
            curr = copyNode.next

        # After the first pass, the list looks like:
        # original1 -> copy1 -> original2 -> copy2 -> ...

        curr = head
        # === Second pass: assign random pointers for the copy nodes ===
        while curr:
            tmp = curr.next  # This is the copy node following tmp
            if curr.random:
                # The copy's random should point to tmp.random's copy
                # tmp.random.next is the copy of tmp.random because of the interleaving
                tmp.random = curr.random.next
            # Move to the next original node (skip the copy)
            curr = curr.next.next

        # === Third pass: separate the interleaved list into original and copied lists ===
        dummy = Node(-1)  # Dummy head for the new copied list
        res = dummy       # Pointer to build the new list
        curr = head        # Reset tmp to head of the original list

        while curr:
            tmp = curr.next  # The copied node to extract
            # Append the copied node to the result list
            res.next = tmp

            # Restore the original list by skipping the copied node
            curr.next = tmp.next

            # Move res forward in the copied list
            res = res.next
            # Move tmp forward in the original list
            curr = tmp.next

        # dummy.next is the head of the deep copied list
        return dummy.next

        # O(n) time complexity where n is the number of nodes in the linked list
        # O(1) space complexity since we don't create extra space  


        


            



        

        