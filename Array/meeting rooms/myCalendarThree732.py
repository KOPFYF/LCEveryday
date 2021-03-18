class Node:
    def __init__(self, start, end, k):
        self.start = start
        self.end = end
        self.k = k
        self.right = self.left = None

class MyCalendarThree2:
    # BST

    def __init__(self):
        self.root = None
        self.k = 0
    def book(self, start: int, end: int) -> int:
        self.root = self.insert(self.root, start, end, 1)
        return self.k
        
    def insert(self, root, start, end, k):
        if start >= end:
            return root
        if not root:
            self.k = max(self.k, k)
            return Node(start, end, k)
        if end <= root.start:
            root.left = self.insert(root.left, start, end, k)
            return root
        if start >= root.end:
            root.right = self.insert(root.right, start, end, k)
            return root
        lefts, lefte, rights, righte = min(start, root.start), max(start, root.start), min(end, root.end), max(end, root.end)
        root.left = self.insert(root.left, lefts, lefte, root.k if lefts == root.start else k)
        root.right = self.insert(root.right, rights, righte, root.k if righte == root.end else k)
        root.k += k
        root.start = lefte
        root.end = rights
        self.k = max(self.k, root.k)
        return root


class MyCalendarThree1:

    def __init__(self):
        self.time = []
        self.k = 0

    def book(self, start: int, end: int) -> int:
        # O(nlogn) sort
        self.time.append((start, 1))
        self.time.append((end, -1))
        self.time.sort()
        
        cnt = 0
        for t, diff in self.time:
            cnt += diff
            self.k = max(self.k, cnt)
        return self.k
        


class MyCalendarThree0:

    def __init__(self):
        self.time = []
        self.k = 0

    def book(self, start: int, end: int) -> int:
        # O(n) insort
        bisect.insort(self.time, (start, 1))
        bisect.insort(self.time, (end, -1))
        
        cnt = 0
        for t, diff in self.time:
            cnt += diff
            self.k = max(self.k, cnt)
        return self.k