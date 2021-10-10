# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 10001
        while l < r:
            mid = (l + r) // 2
            if reader.get(mid) == 2**31 - 1 or reader.get(mid) > target:
                r = mid
            elif reader.get(mid) < target:
                l = mid + 1
            else:
                return mid

        return -1
        # return l if reader.get(l) == target else -1


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution1:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # find the rough range first
        hi = 1
        while reader.get(hi) < target: hi <<= 1
        lo = hi >> 1
        while lo <= hi:
            mid = lo + hi >> 1
            if reader.get(mid) < target: lo = mid + 1
            elif reader.get(mid) > target: hi = mid - 1
            else: return mid
        return -1