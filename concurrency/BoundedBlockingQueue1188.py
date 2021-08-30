from collections import deque
from threading import Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.locke, self.lockd = Lock(), Lock()
        self.dq = deque()
        self.capacity = capacity
        self.lockd.acquire() # Lock dequeue first because it's empty
        
    def enqueue(self, element: int) -> None:
        self.locke.acquire()
        self.dq.append(element)
        if len(self.dq) < self.capacity:
            self.locke.release()
        if self.lockd.locked(): # if dequeue locked, release it since now we have element
            self.lockd.release()
        
    def dequeue(self) -> int:
        self.lockd.acquire()
        res = self.dq.popleft()
        if len(self.dq):
            self.lockd.release()
        if res and self.locke.locked(): # if enqueue locked, release it since now we have element
            self.locke.release()
        return res

    def size(self) -> int:
        return len(self.dq)
        