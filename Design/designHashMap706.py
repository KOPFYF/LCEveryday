class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next
        

class MyHashMap:
    # like Hash set, still many to one mapping, but with a simple hash function
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [Node() for _ in range(1000)]
        
    def _hash(self, key):
        return key % len(self.data)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        h = self._hash(key)
        cur = self.data[h]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value) # put it at chain's end
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        h = self._hash(key)
        cur = self.data[h]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        h = self._hash(key)
        cur = self.data[h]
        while cur.next:
            if cur.next.key == key:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = None
                return 
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



# https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
# using just arrays, direct access table
# using linked list for chaining
class ListNode:
    def __init__(self, key, val):
        """
        Initialize your data structure here.
        """
        self.pair = (key, val)
        self.next = None
        
class MyHashMap1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.h = [None] * self.m
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.m
        if self.h[idx] == None:
            self.h[idx] = ListNode(key, value)
        else:
            cur = self.h[idx]
            # loop to the end of current chain
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.m
        cur = self.h[idx]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.m
        cur = prev = self.h[idx]
        if not cur: 
            return
        if cur.pair[0] == key:
            self.h[idx] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)