'''
for bigger picture
mean minimizes total distance for euclidian distance
median minimzes total distance for absolute deviation
mode minimizes distance for indicator function

these are classic statistical properties for MLE / MAP in point estimation.

A better view is we can think i and j as two meet points. All the people in [0, i] go to meet at i and all the people in [j, n - 1] meet at j. We let left = sum(vec[:i+1]), right = sum(vec[j:]), which are the number of people at each meet point, and d is the total distance for the left people meet at i and right people meet at j.

If we increase i by 1, the distance will increase by left since there are 'left' people at i and they just move 1 step. The same applies to j, when decrease j by 1, the distance will increase by right. To make sure the total distance d is minimized we certainly want to move the point with less people. And to make sure we do not skip any possible meet point options we need to move one by one.
'''

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # find median independently
        row_sum = map(sum, grid) # size = len(grid)
        col_sum = map(sum, zip(*grid)) # size = len(grid[0])
        
        # print(list(row_sum), list(col_sum)) 
        # [2, 0, 1] [1, 0, 1, 0, 1]
        #  i=1,j=-1       i=3,j=1
        #  i=0,j=0        i=2,j=2(method 2)
        
        def minTotalDistance1D(v):
            # 2 ptrs, O(n)
            # left = sum(vec[:i+1]), right = sum(vec[j:])
            v = list(v)
            i, j = 0, len(v) - 1
            d = left = right = 0
            while i <= j + 1:
                if left < right:
                    d += left
                    left += v[i]
                    i += 1
                else:
                    d += right
                    right += v[j]
                    j -= 1
            print(i, j)
            return d
        
        def minTotalDistance1D_2(vec):
            vec = list(vec)
            i, j = -1, len(vec)
            d = left = right = 0
            while i < j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            print(i, j)
            return d

        # print(minTotalDistance1D(row_sum), minTotalDistance1D(col_sum)) # 2, 4
        return minTotalDistance1D_2(row_sum) + minTotalDistance1D_2(col_sum)
                    