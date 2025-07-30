# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Problem Intuition:
        - The input linked lists represent numbers in reverse order.
          For example, the number 342 is represented as 2 -> 4 -> 3.
        - We need to simulate elementary addition, digit by digit, from least significant to most significant.
        - At each digit, we add the corresponding digits from both lists and any carry from the previous addition.
        - The result should also be returned as a linked list in reverse order.
        """
        dummy = ListNode()          # Dummy head simplifies result list creation
        current = dummy             # Pointer to the current end of the result list
        carry = 0                   # Initialize carry to 0
        # Loop through both lists until we've processed all digits and any leftover carry
        while l1 or l2 or carry:
            # Get values from the current nodes or 0 if one list is shorter
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry # Add the two digits and the carry from the previous step
            digit = total % 10 # The new digit is the units place of the total
            carry = total // 10 # Update the carry for the next iteration
            current.next = ListNode(digit) # Add the digit to the result list
            current = current.next
            # Advance the input list pointers if possible
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next # Return the result list (skipping the dummy node)
        # ---------------------------------------------------
        # Time Complexity: O(max(n, m))
        # - n: length of l1
        # - m: length of l2
        # - We traverse both lists once, doing constant work per node.

        # Space Complexity: O(max(n, m))
        # - We create one new node per digit in the result.
        # - In the worst case, the result has one extra digit (from final carry).
        # - Auxiliary space is O(1) (only a few pointers and integers used).


