# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # generateor
    def __init__(self, nestedList: [NestedInteger]):
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for xx in gen(x.getList()):
                        yield xx
        self.genList = gen(nestedList)
        self.prev = next(self.genList, None)
            
    def next(self) -> int:
        tmp = self.prev
        self.prev = next(self.genList, None)
        return tmp
    
    def hasNext(self) -> bool:
        return self.prev != None


class NestedIterator2(object):
    # deque/stack
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        
        self.queue = collections.deque(nestedList)
        
    def next(self):
        """
        :rtype: int
        """
        return self.queue.popleft().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.queue:
            if self.queue[0].isInteger():
                return True
            else:
                first = self.queue.popleft()
                self.queue.extendleft(first.getList()[::-1])
        return False         


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())