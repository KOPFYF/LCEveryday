class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # heap
        h = set([1])
        heap = [1]
        for _ in range(n):
            a = heappop(heap) # min heap pop n times
            for i in [2,3,5]:
                m = a * i
                if m not in heap:
                    heappush(heap, m) # push into heap for all primes*a
                    h.add(m)
        return a