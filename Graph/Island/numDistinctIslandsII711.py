class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n else 0
        
        def dfs(i,j):
            if 0 <= i < n and 0 <= j < m and grid[i][j]==1:
                grid[i][j] = -1
                path.append([i, j])
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
                
        def normalize(path): 
            # encoding the path(a 2d list of positions) into a 1d list
            # compute all possible rotations/reflections of it 
            # and then sort them using the default comparison. 
            # The first representation in this order is then the canonical one.
            # https://en.wikipedia.org/wiki/Dihedral_group
            res=[[] for _ in range(8)]
            for x, y in path:
                # given n points, res shape is n * 8
                res[0].append([x, y])
                res[1].append([x, -y])
                res[2].append([-x, y])
                res[3].append([-x, -y])   
                res[4].append([y, x])
                res[5].append([y, -x])
                res[6].append([-y, x])
                res[7].append([-y, -x])                             
            for r in res:
                # loop each point, r size is 8
                r.sort()
                x0, y0 = r[0]
                for p in r:
                    p[0] -= x0
                    p[1] -= y0
            res.sort()
            return tuple(c for r in res[0] for c in r) # flatten
        
        res = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j)
                    print('path before norm', path)
                    path = normalize(path)
                    print('path after norm', path)
                    res.add(path)
        return len(res)

'''
path before norm [[0, 0], [0, 1], [1, 0]]
[[[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, -1], [1, 0]], [[0, 0], [1, -1], [1, 0]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, 1]]]
[[0, 0], [0, 1], [1, 0]]
path after norm (0, 0, 0, 1, 1, 0)
path before norm [[2, 4], [3, 4], [3, 3]]
[[[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, -1], [1, 0]], [[0, 0], [1, -1], [1, 0]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, 1]]]
[[0, 0], [0, 1], [1, 0]]
path after norm (0, 0, 0, 1, 1, 0)
'''