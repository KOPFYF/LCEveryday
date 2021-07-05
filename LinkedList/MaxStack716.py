from collections import defaultdict
from heapq import heappush, heappop, heapify


class DoubleLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None
    

class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        
        self.stack = DoubleLinkedList(float('-inf')) # init a dummy node
        self.last = self.stack                       # reference the stack tail
        self.heap = []
        self.hmap = defaultdict(list)
        

    def push(self, x: int) -> None:
        # O(logn)
        node = DoubleLinkedList(x)
        
        # update the tail
        self.last.next = node
        node.pre = self.last
        self.last = node
        
        # push -x to the min heap
        heappush(self.heap, -x)
        
        # append node the the map entry
        self.hmap[x].append(node)
        
    def pop(self) -> int:
        # O(1)
        # pop from the stack and remove from map
        num = self.last.val
        self.last = self.last.pre
        self.last.next = None
        
        self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        return num

    def top(self) -> int:
        # O(1)
        return self.last.val

    def peekMax(self) -> int:
        # O(logN)
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the the poped elements from heap
        while -self.heap[0] not in self.hmap:
            heappop(self.heap)
        
        return -self.heap[0]

    def popMax(self) -> int:
        # O(logN)
        # get the top-most node from map
        num = self.peekMax()
        node = self.hmap[num].pop()
        if not self.hmap[num]:
            del self.hmap[num]
        
        # update the tail reference
        if node == self.last:
            self.last = self.last.pre
        
        # remove the node from stack
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        return num


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()




class DoubleLinkedList:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MaxStack2:
    # using list

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.l.append(x)


    def pop(self):
        """
        :rtype: int
        """
        return self.l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]


    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.l)


    def popMax(self):
        """
        :rtype: int
        """
        self.l = self.l[::-1]
        max_num = self.l.pop(self.l.index(max(self.l))) # to pop the top-most one
        self.l = self.l[::-1]
        return max_num