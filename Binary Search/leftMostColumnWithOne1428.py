# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # binary search O(nlogm)
        n, m = binaryMatrix.dimensions()
        
        def binary_search(j, m):
            # logm
            l, r = 0, m
            while l < r:
                mid = (l + r) // 2
                if not binaryMatrix.get(j, mid):
                    l = mid + 1
                else:
                    r = mid
            return l
        
        res = m            
        for j in range(n):
            res = min(res, binary_search(j, m))
        return res if res < m else -1
            