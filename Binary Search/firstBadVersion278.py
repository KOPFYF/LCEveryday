class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            # when while loop end, l = r = the first bad version
            m = l + (r - l) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
        return l