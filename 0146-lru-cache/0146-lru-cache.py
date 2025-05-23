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
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Delete the node DLL
            self.delete(node)
            # Move to the front of the head
            self.move_front_of_head(node)
            return node.value
        else:
            return -1

    def delete(self, node):
        node_prev = node.prev
        node_after = node.next
        node_prev.next = node_after
        node_after.prev = node_prev

    def move_front_of_head(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node

    def put(self, key: int, value: int) -> None:
        # print("key", key)
        # print("value", value)
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # Delete the node DLL
            self.delete(node)
            # Move to the front of the head
            self.move_front_of_head(node)
            self.cache[key] = node
        else:
            if len(self.cache) >= self.capacity:
                node = self.tail.prev
                # Eviction Policy
                # Deleting the Node
                # print(self.cache)
                # print(node.value)
                del self.cache[node.key]
                self.delete(node)

            node = Node(key, value)
            # Insert in the front of the head
            self.move_front_of_head(node)
            self.cache[key] = node

 



        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)