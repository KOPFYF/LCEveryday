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