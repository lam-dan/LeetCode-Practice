class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.count = 1
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node(None, None) #Sentinel Dummy Head Nodes
        self.tail = Node(None, None) #Sentinel Dummy Tail Nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after_head(self, node: Node):
        tmp = self.head.next
        node.next = tmp
        node.prev = self.head
        self.head.next = node
        tmp.prev = node
        self.size += 1
    
    def delete(self, node: Node):
        node_prev = node.prev
        node_after = node.next
        node_prev.next = node_after
        node_after.prev = node_prev
        self.size -= 1

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {} # contains map of keys and Nodes
        # Maps frequency counts to a doubly linked list of nodes at that frequency
        self.freq = defaultdict(DLL)  
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

    def update_freq_list(self, node):
        # Grab doubly linked list of nodes at that frequency
        dll_at_freq = self.freq[node.count] 
        dll_at_freq.delete(node) # remove the node from that dll at the frequency

        if (node.count == self.min_freq and dll_at_freq.size == 0):
            self.min_freq += 1
        
        node.count += 1
        self.freq[node.count].insert_after_head(node)


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Update node in hashmap of frequency list because it has been accessed
            self.update_freq_list(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_freq_list(node)
        else:
            if self.size >= self.capacity:
                dll_at_min_freq = self.freq[self.min_freq]
                node_to_evict = dll_at_min_freq.tail.prev
                dll_at_min_freq.delete(node_to_evict)
                del self.cache[node_to_evict.key]
                self.size -= 1

            new_node = Node(key, value)
            self.freq[1].insert_after_head(new_node)
            self.cache[key] = new_node
            self.min_freq = 1
            self.size += 1







        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)