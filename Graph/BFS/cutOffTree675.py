

class Solution_BFS_TLE(object):
    def cutOffTree(self, G):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not G or not G[0]: return -1
        m, n = len(G), len(G[0])
        trees = []
        for i in xrange(m):
            for j in xrange(n):
                if G[i][j] > 1:
                    trees.append((G[i][j], i, j))
        trees = sorted(trees)
        count = 0
        cx, cy = 0, 0
        for h, x, y in trees:
            step = self.BFS(G, cx, cy, x, y)
            if step == -1:
                return -1
            else:
                count += step
                G[x][y] = 1
                cx, cy = x, y
        return count

    def BFS(self, G, cx, cy, tx, ty):
        m, n = len(G), len(G[0])
        visited = [[False for j in xrange(n)] for i in xrange(m)]
        Q = collections.deque()
        step = -1
        Q.append((cx, cy))
        while len(Q) > 0:
            size = len(Q)
            step += 1
            for i in xrange(size):
                x, y = Q.popleft()
                # visited[x][y] = True
                if x == tx and y == ty:
                    return step
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y-1), (x, y + 1)]:
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or G[nx][ny] == 0 or visited[nx][ny]:
                        continue
                    Q.append((nx, ny))
                    visited[x][y] = True
        return -1