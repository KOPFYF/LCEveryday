class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.s.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.s) == 0:
            return None
        else:
            return self.s[len(self.s) - 1][1]