class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 binary search
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        r = self.binSearch(matrix, target, 0, len(matrix) - 1)
        if r == -1:
            return False
        c = self.binSearchCol(matrix, target, 0, len(matrix[r]) - 1, r)
        return c != -1
    
        
    def binSearch(self, matrix, target, l, h):
        while l <= h:
            m = (h + l) / 2
            # print m
            if matrix[m][0] <= target and matrix[m][len(matrix[m]) - 1] >= target:
                return m
            if matrix[m][0] > target:
                h = m - 1
            else:
                l = m + 1
        return -1

    def binSearchCol(self, matrix, target, l, h, r):
        while l <= h:
            m = (h + l) / 2
            if matrix[r][m] == target:
                return m
            if matrix[r][m] > target:
                h = m - 1
            else:
                l = m + 1
        return -1
        
        # O(m + logn)
        def bisect(row, target):
            '''
            l --- mid --(t)- r
            '''
            l, r = 0, len(row)
            while l < r:
                mid = (l + r) // 2
                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid
                else:
                    return True
            return False
        
        m, n = len(matrix), len(matrix[0])
        i = 0
        while i < m:
            row = matrix[i]
            if row[0] <= target <= row[-1]:
                return bisect(row, target)
            i += 1
        return False
                    