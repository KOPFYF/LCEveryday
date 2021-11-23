class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # decreasing monotonic stack
        cnt = 1
        while self.stack and price >= self.stack[-1][0]:
            cnt += self.stack.pop()[1]
            # print(self.stack, price, cnt)
        self.stack.append((price, cnt))
        return cnt