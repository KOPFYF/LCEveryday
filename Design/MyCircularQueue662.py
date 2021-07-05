'''
Implementing a circular queue using linked lists defeats the purpose of circular queues (Space Reusability). I don't think interviewer would like to see linked list implementation of circular queue.
It would be good to remove the linked list implementation from the solution.
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.front = 0
        self.rear = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size # rear idx++, % for circle/out of range
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # self.queue[self.front] = None # ? release the memory
        self.front = (self.front + 1) % self.max_size # front idx++
        self.size -= 1
        return True
        
    def Front(self) -> int:
        return self.queue[self.front] if self.size else -1

    def Rear(self) -> int:
        return self.queue[self.rear] if self.size else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()