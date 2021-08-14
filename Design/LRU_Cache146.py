class DLinkedlist:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        
class LRUCache:
    # Space O(capacity), each function O(1), July 7 2021

    def __init__(self, capacity: int):
        self.head = DLinkedlist(-1, -1)
        self.tail = DLinkedlist(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        

    def get(self, key: int) -> int:
        # Return the value of the key if the key exists, otherwise return -1
        if key in self.cache:
            node = self.cache[key]
            self.remove_to_head(node)
            return node.value
        else:
            return -1
        
    def remove_to_head(self, node):
        # O(1)
        # 1. remove the node
        # 2. put the node to the head
        self.remove(node)
        self.add(node)
        
    def remove(self, node):
        # 1. remove the node in the middle, O(1)
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre
        
        
    def add(self, node):
        # put the node to the head, O(1)
        tmp = self.head.next
        tmp.prev = node
        node.next = tmp
        self.head.next = node
        node.prev = self.head
        
         
    def put(self, key: int, value: int) -> None:
        # O(1)
        # Update the value of the key if the key exists. 
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_to_head(node)
        # Otherwise, add the key-value pair to the cache. 
        else:
            node = DLinkedlist(key, value)
            self.cache[key] = node
            self.add(node)
            # If the number of keys exceeds the capacity from this operation, evict the least recently used key.
            self.size += 1
            if self.size > self.capacity:
                tail = self.pop_tail()
                self.size -= 1
                del self.cache[tail.key]
                
                
    def pop_tail(self):
        # remove the tail node, O(1)
        tail = self.tail.prev
        self.remove(tail)
        return tail
        
        # tail2nd = tail.prev
        # tail2nd.next = self.tail
        # self.tail.prev = tail2nd
        # return tail



class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache0:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        # set the new node to the end
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n

        # remove least recently used node in the head
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        # remove node in between
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        # add node to the tail
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


class LRUCache1:
    # implement a double linked list using bfr/nxt pointers

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.nxt, self.bfr = {}, {}
        self.head, self.tail = '^', '$'
        self.connect(self.head, self.tail)
     
    def connect(self, a, b):
        self.nxt[a], self.bfr[b] = b, a # circular linked list

    def delete(self, key):
        # remove a node in the linked list
        self.connect(self.bfr[key], self.nxt[key])
        del self.bfr[key], self.nxt[key], self.cache[key]
        
    def append(self, k, v):
        # bfr -> k -> tail, insert latest (k, v)
        self.cache[k] = v
        self.connect(self.bfr[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.nxt[self.head]) # remove head
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)
        self.append(key, value)


class LRUCache_Orderdict:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        # Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist
        self.cache.move_to_end(key, last=True) # move to last
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False) # returned in LIFO order if last is true or FIFO order if false.