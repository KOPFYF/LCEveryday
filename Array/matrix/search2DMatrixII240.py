'''
Starting from Top-Right corner:
If current grid M[r][c] is smaller than target x, there is no need to consider M[r][ :c] since all the grids on the left must be smaller as well. So, x must be in the rows below and we can safely make r += 1.
We keep moving M[r][c] downwards until it's larger x, then we can safely move leftwards and make c -= 1 since all the grids in M[ :r][c ] would be larger than x.
During the search, if x is found, we return True. Otherwise, we can either move downwards or leftwards safely.
If we reach left-bottom corner without hitting x, then target is not in the matrix.

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # move from upper right to bottom left, O(m+n)
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0: # overflow
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            else:
                return True
        return False



class Solution:
    def searchMatrix(self, matrix, target):
        # binary search O(mlogn)
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        while i < m and target >= matrix[i][0]: # only when target > start of row
            low, high = 0, n
            while low < high: # bisect each row
                mid = (low + high) // 2
                if target > matrix[i][mid]:
                    low = mid + 1
                elif target < matrix[i][mid]:
                    high = mid
                else:
                    return True
            i += 1 # row by row search
        return False