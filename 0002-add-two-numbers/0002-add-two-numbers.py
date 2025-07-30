# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        dummy = ListNode()
        ptr3 = dummy
        carry_value = 0

        while ptr1 or ptr2:
            if ptr2 and ptr1 is None:
                ptr1_val = 0
                ptr2_val = ptr2.val
            elif ptr1 and ptr2 is None:
                ptr1_val = ptr1.val
                ptr2_val = 0
            elif ptr1 and ptr2:
                ptr1_val = ptr1.val
                ptr2_val = ptr2.val
            else:
                break

            total = ptr1_val + ptr2_val

            if total // 10: # Calculates values > 10
                stay_value = total % 10
                new_node = ListNode(stay_value + carry_value)
                carry_value = 1 # single digit max is 9 + 9 = 18
            else:
                new_total = total + carry_value
                if new_total // 10:
                    stay_value = new_total % 10
                    new_node = ListNode(stay_value)
                    carry_value = 1
                else:
                    new_node = ListNode(total + carry_value)
                    carry_value = 0
            if ptr1:
                ptr1 = ptr1.next 
            if ptr2:
                ptr2 = ptr2.next 
            
            ptr3.next = new_node
            ptr3 = ptr3.next
            print("dummy.next", dummy)
        
        if carry_value:
            new_node = ListNode(carry_value)
            ptr3.next = new_node

        return dummy.next

            


