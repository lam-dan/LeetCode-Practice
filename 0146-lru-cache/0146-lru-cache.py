from typing import Any
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #Initialize with empty, avoid using defaultdict since we don't want default intializes
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)

        self.left, self.right = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Return value of the key if it exists otherwise, return -1
    def get(self, key) -> Any:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert_after_head(node)
            return node.value
        else: 
            return -1

    def delete(self, node: Node):
        node_previous = node.prev
        node_after = node.next
        node_previous.next = node_after
        node_after.prev = node_previous


    def insert_after_head(self, node: Node):
        current_after_head = self.head.next
        node.next = current_after_head
        node.prev = self.head
        self.head.next = node
        current_after_head.prev = node

    # O(1) capacity
    # Check if we don't have space, remove the least recently used
    # otherwise do nothing
    # Put the value in the dictionary
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.insert_after_head(node)
        # If not in the map
        if key not in self.cache:
            # Remove the least recently used
            # Multiple Conditions:
            # 1) Cache is filled up
            if len(self.cache) >= self.capacity:
                node = self.tail.prev
                print(node.key)
                del self.cache[node.key]
                self.delete(node)
            node = Node(key, value)
            self.cache[key] = node
            self.insert_after_head(node)


        