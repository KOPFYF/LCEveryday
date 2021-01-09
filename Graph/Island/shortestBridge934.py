class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # DFS to find the first island, then BFS
        n, step, bfs = len(A), 0, []
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            A[i][j] = -1 # marked as seen
            bfs.append((i, j))
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
                    
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    dfs_i, dfs_j = i, j
                    break
        dfs(dfs_i, dfs_j)
        # print(bfs)          
        while bfs:
            nxt_bfs = []
            for i, j in bfs:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            nxt_bfs.append((x, y))
            step += 1
            bfs = nxt_bfs