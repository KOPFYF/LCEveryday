class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = [] # main stack to store the queue
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # O(n), reverse and reverse again
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
                

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]
    

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1



class MyQueue2:
    # push O(1), pop amortized O(1)
    def __init__(self):
        self.s1 = [] # input 
        self.s2 = [] # output

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        # peek does the moving from input to output stack.
        # Each element only ever gets moved like that once, though, 
        # and only after we already spent time pushing it, 
        # so the overall amortized cost for each operation is O(1).
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2