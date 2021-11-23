class ProductOfNumbers:

    def __init__(self):
        self.presum = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.presum = [1] # reset
        else:
            self.presum.append(self.presum[-1] * num)
        

    def getProduct(self, k: int) -> int:
        # You can assume that always the current list has at least k numbers
        if k >= len(self.presum):
            return 0 # contains 0
        return self.presum[-1] // self.presum[-k-1]