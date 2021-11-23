"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        # recursion
        def isLeaf(board):
            tmp = board[0][0]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != tmp:
                        return False
            return True
        
        n = len(grid)
        half = n // 2
        if isLeaf(grid):
            # If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null
            return Node(grid[0][0] == 1, True, None, None, None, None)
        else:
            # If the current grid has different values, set isLeaf to False and set val to any value
            return Node('*', False, \
                       self.construct([row[:half] for row in grid[:half]]), \
                       self.construct([row[half:] for row in grid[:half]]), \
                       self.construct([row[:half] for row in grid[half:]]), \
                       self.construct([row[half:] for row in grid[half:]]))
        
        # iteration
        N = len(grid)
        new_grid = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                new_grid[i].append(Node(grid[i][j] == 1, True, None, None, None, None))
        while N > 0:
            N //= 2
            for i in range(N):
                for j in range(N):
                    a = new_grid[i * 2][j * 2]
                    b = new_grid[i * 2][j * 2 + 1]
                    c = new_grid[i * 2 + 1][j * 2]
                    d = new_grid[i * 2 + 1][j * 2 + 1]
                    if a.val == b.val == c.val == d.val and a.val != '*':
                        new_grid[i][j] = Node(a.val, True, None, None, None, None)
                    else:
                        new_grid[i][j] = Node('*', False, a, b, c, d)
        return new_grid[0][0]

            