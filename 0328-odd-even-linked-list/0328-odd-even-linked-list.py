# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the linked list is empty, return None immediately
        if head is None:
            return None

        # Initialize two pointers:
        # odd -> points to the first node (odd index)
        # even -> points to the second node (even index)
        odd = head
        even = odd.next
        
        # Save the head of the even list so we can append it later
        evenhead = even

        # Loop until there are no more even nodes or no more nodes after an even node
        while even and even.next:
            # Link the current odd node to the next odd node (skip the even node)
            odd.next = even.next
            odd = odd.next  # Move odd pointer forward

            # Link the current even node to the next even node (skip the odd node)
            even.next = odd.next
            even = even.next  # Move even pointer forward

        # Append the even list after the odd list
        odd.next = evenhead

        # Return the head of the rearranged linked list
        return head