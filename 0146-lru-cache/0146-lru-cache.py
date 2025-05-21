class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail = Node(None, None)
        self.head = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # O(1) operation since we're accessing the dictionary
    def get(self, key: int) -> int: 
        if key in self.cache:
            node = self.cache[key]
            # Add moving node to the beginning of the head because it's been recently used
            self.delete(node) # delete node
            self.insert_after_head(node) # move node to the head
            return node.value
        else:
            return -1

    # Put operation update a value in the cache if exists
    # Put operation to add value 
    # capacity
    def put(self, key: int, value: int) -> None:
        size = self.get_size()
        # 2 Cases
        # Eviction where size is greater than capacity
        # Remove a node from the tail
        if size >= self.capacity:
            # Least recently used is not self.tail because a doubly linked list
            # has dummy nodes at head and tail
            node = self.tail.prev
            del self.cache[node.key]
            self.delete(node)
        # Not greater than capacity
        # We can put a value in the dictionary and also update it
        # to be recently used by moving it to the head
        if key in self.cache:
            # Update the value in the cache
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.insert_after_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_after_head(node)

    def insert_after_head(self, node: Node):
        tmp = self.head.next
        node.next = tmp
        node.prev = self.head
        self.head.next = node
        tmp.prev = node

    def delete(self, node: Node):
        node_prev = node.prev
        node_after = node.next
        node_prev.next = node_after
        node_after.prev = node_prev

    def get_size(self) -> int:
        return len(self.cache)


    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)