# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

'''
000001
000000
000011
011111
000111
000000
001111

0000**
0000*0
000**1
****11
*00111
*00000
*01111
*
'''
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # O(m + n)
        m, n = binaryMatrix.dimensions()
        i, j, leftMost = 0, n - 1, -1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                leftMost = j
                j -= 1
        return leftMost