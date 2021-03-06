class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        u, d, l, r = 0, m - 1, 0, n - 1
        while True: # corner case in the center
            # left to right
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1 # first row is done, up++
            if u > d: break
            
            # top to bottom on the right side
            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r: break
            
            # right to left
            for i in range(r, l - 1, -1):
                res.append(matrix[d][i])
            d -= 1 
            if u > d: break
                
            # bottom to top on the left side
            for i in range(d, u - 1, -1):
                res.append(matrix[i][l])
            l += 1 
            if l > r: break
            
        return res


class Solution1(object):
    def spiralOrder(self, matrix):
        arr = []
        while matrix:
            #extend the top row
            arr.extend(matrix.pop(0))
            #extend the right colomn
            if matrix:
                for i in range(len(matrix)):
                    if matrix[i]:
                        arr.append(matrix[i].pop())
            #extend the bottom row
            if matrix:
                arr.extend(matrix.pop()[::-1])
            #extend the left colomn
            if matrix:
                for i in range(len(matrix)-1,-1,-1):
                    if matrix[i]:
                        arr.append(matrix[i].pop(0))
        return arr