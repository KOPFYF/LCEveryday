class Solution:
    # sampling with weight
    # Prefix Sums with Linear Search/Binary Search

    def __init__(self, w: List[int]):
        self.presum = [0] * len(w)
        self.presum[0] = w[0]
        for i in range(1, len(w)):
            self.presum[i] = self.presum[i - 1] + w[i]
        # print(self.presum)
         

    def pickIndex_slow(self) -> int:
        # O(n)
        # random.random gives (0, 1), so it gives (0, max)
        target = self.presum[-1] * random.random()
        for i, pre in enumerate(self.presum):
            if pre >= target:
                return i
        
        
    def pickIndex(self) -> int:
        # O(logn)
        target = self.presum[-1] * random.random()
        l, r = 0, len(self.presum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.presum[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l 