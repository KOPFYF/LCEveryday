# ! it has bug!

class DoubleLinkedListNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = 1
        
class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLinkedListNode(-1, -1)
        self.tail = DoubleLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def remove(self, node):
        # remove node in the middle
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
    
    def append(self, node):
        # append the node to the head of the linked list
        curhead = self.head.next
        node.next = curhead
        curhead.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1
    
    def pop(self, node=None):
        # remove the referenced node. 
        # If None is given, remove the one from tail, which is the least recently used
        if self.size == 0:
            return
        if not node:
            # node is None
            node = self.tail.prev
        else:
            self.remove(node)
            self.size -= 1
        return node
            
        
class LFUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.size = 0
        self.cache = {} # key: node
        # key is freq, value is linked list, each freq will have a seperate list
        self.freqs = defaultdict(DoubleLinkedList) 
        self.minfreq = 0
        
    def update(self, node):
        # pop the node from the old DLinkedList (with freq `f`)
        # append the node to new DLinkedList (with freq `f+1`)
        # if old DlinkedList has size 0 and self._minfreq is `f`, update self._minfreq to `f+1`
        print('update:', node)
        freq = node.freq
        self.freqs[freq].pop(node) 
        if not self.freqs[freq] and self.minfreq == freq: # update the least freq
            self.minfreq += 1
        node.freq += 1
        self.freqs[node.freq].append(node) 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                node = self.freqs[self.minfreq].pop() # node from min freq, and least recently used
                del self.cache[node.key]
                self.size -= 1
            
            node = DoubleLinkedListNode(key, value)
            self.cache[key] = node
            self.freqs[1].append(node)
            self.minfreq = 1
            self.size += 1