class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev
    
    def move_to_front(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.move_to_front(node)
            return node.value
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.move_to_front(node)
            self.cache[key] = node
        else:
            # To add key-value pair to the cache
            # Need to check capacity first
            if len(self.cache) >= self.capacity:
                #Evict LRU
                node = self.tail.prev
                self.delete(node)
                del self.cache[node.key]
            # Add to cache
            node = Node(key, value)
            self.move_to_front(node)
            self.cache[key] = node


            



    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)