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
        del self.cache[node.key]
        # Grab doubly linked list of nodes at that frequency
        dll_at_freq = self.freq[node.count] 
        dll_at_freq.delete(node) # remove the node from that dll at the frequency

        if (node.count == self.min_freq and dll_at_freq.size == 0):
            self.min_freq += 1
        
        next_higher_freq_list = DLL()
        next_freq_count = node.count + 1

        if next_freq_count in self.freq:
            next_higher_freq_list = self.freq[next_freq_count]

        node.count += 1
        next_higher_freq_list.insert_after_head(node)
        self.freq[node.count] = next_higher_freq_list
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Update node in hashmap of frequency list because it has been accessed
            self.update_freq_list(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if self.capacity == 0:
        #     return
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_freq_list(node)
        else:
            if self.size >= self.capacity:
                dll_at_min_freq = self.freq[self.min_freq]
                # Remove the node before the dummy tail's keys from the cache
                del self.cache[dll_at_min_freq.tail.prev.key]
                # Remove the node before the dummy tail from the freq
                dll_at_min_freq.delete(dll_at_min_freq.tail.prev)
                self.size -= 1

            self.size += 1 # Increment size
            self.min_freq = 1 # Reset min frequency back to 1

            new_dll_at_freq = DLL()
            if self.min_freq in self.freq:
                new_dll_at_freq = self.freq[self.min_freq]
            
            new_node = Node(key, value)
            new_dll_at_freq.insert_after_head(new_node)
            self.cache[key] = new_node
            self.freq[self.min_freq] = new_dll_at_freq






        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)