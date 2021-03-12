class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        res, d = 0, defaultdict(int)
        for t in time:
            t %= 60
            res += d[(60 - t) % 60]
            d[t % 60] += 1
        return res