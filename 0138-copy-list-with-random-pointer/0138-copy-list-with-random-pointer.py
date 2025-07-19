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
        dic = {}  # Dictionary to map original nodes to their corresponding copied nodes

        # First pass: copy each node by value only, no next/random yet
        while tmp is not None:
            dic[tmp] = Node(tmp.val)  # Create a new node with the same value as the original
            tmp = tmp.next  # Move to the next node in the original list

        tmp = head  # Reset tmp to start from head again
        # Second pass: assign next and random pointers for each copied node
        while tmp is not None:
            copyNode = dic[tmp]  # The copied node corresponding to the current original node

            # Set 'next' pointer of the copied node:
            # If tmp.next is None, we assign None. Otherwise, we map it to the copied node.
            copyNode.next = dic[tmp.next] if tmp.next is not None else None

            # Set 'random' pointer of the copied node:
            # If tmp.random is None, assign None. Otherwise, map it to the copied node.
            copyNode.random = dic[tmp.random] if tmp.random is not None else None

            tmp = tmp.next  # Move to the next node in the original list

        # WHY WE RETURN dic[head]:
        # tmp is now None because the while loop finished traversing the list.
        # If we returned dic[tmp], it would be equivalent to dic[None], causing a KeyError.
        # head still points to the first node of the original list.
        # dic[head] gives us the corresponding copied head node, which is the correct return value.
        return dic[head]

        

        