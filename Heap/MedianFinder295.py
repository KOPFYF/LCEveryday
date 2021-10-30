class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # a max heap, -num
        self.large = [] # a min heap, num

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # heapq.heappushpop(heap, item)
        # 将 item 放入堆中，然后弹出并返回 heap 的最小元素。该组合操作比先调用  heappush() 再调用 heappop() 运行起来更有效率
        # so that large size = small size + 1
        if len(self.large) == len(self.small):
            # if 2 heaps have equal size, push into large
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # if 2 heaps dont have equal size, push into small
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])