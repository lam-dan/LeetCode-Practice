class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
        self.head.prev = None

    def move_to_front(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node

    def delete(self, node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.delete(node)
            self.move_to_front(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        # If key doesn't exists
        if key not in self.map:

            if len(self.map) >= self.capacity:
                # Start LRU eviction process 
                prev_node = self.tail.prev
                self.delete(prev_node)
                del self.map[prev_node.key]
                node = Node(value, key)
                self.move_to_front(node)
                self.map[key] = node
            else:
                # Create node and link to our doubly linked list
                node = Node(value, key)
                self.move_to_front(node)
                # Add to our dictionary
                self.map[key] = node

        elif key in self.map:  # If key does exists
            # Grab the node 
            node = self.map[key]
            self.delete(node)
            new_node = Node(value, key)
            self.move_to_front(new_node)
            self.map[key] = new_node
            # Update our linked list and move the node to the front

# obj = LRUCache(2)
# obj.put(1,1,)
