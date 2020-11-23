class ProductOfNumbers(object):

    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(self.prefix_prod[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.prefix_prod):
            # encounter a zero
            return 0
        else:
            return self.prefix_prod[-1] / self.prefix_prod[-k - 1]