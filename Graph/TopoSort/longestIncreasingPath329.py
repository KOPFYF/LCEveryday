class Solution_topo(object):
    def longestIncreasingPath(self, M):        
        # topo-sort
        if not M: return 0
        graph = defaultdict(list)
        indegree = defaultdict(int)
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                # (i, j) start, (x, y) end, if inc, build edge
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and M[i][j] < M[x][y]:
                        graph[(i, j)].append((x, y))
                        indegree[(x, y)] += 1
        # bfs level by level because we need max path len
        dq = deque([(i, j) for i in range(m) for j in range(n) if not indegree[(i, j)]])
        res = 0
        while dq:
            res += 1
            for _ in range(len(dq)):
                cur = dq.popleft()
                for nxt in graph[cur]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        dq.append(nxt)
        return res


class Solution_dp_td(object):
    def longestIncreasingPath(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # DFS
        if not M: return 0
        m, n = len(M), len(M[0])
        dp = [[0] * n for i in range(m)]
        
        def dfs(i, j):
            if not dp[i][j]:
                cur = M[i][j]
                dp[i][j] = 1 + max(
                dfs(i - 1, j) if i - 1 >= 0 and cur > M[i - 1][j] else 0,
                dfs(i + 1, j) if i + 1 < m and cur > M[i + 1][j] else 0,
                dfs(i, j - 1) if j - 1 >= 0 and cur > M[i][j - 1] else 0,
                dfs(i, j + 1) if j + 1 < n and cur > M[i][j + 1] else 0)
            return dp[i][j]
            
        return max(dfs(x, y) for x in range(m) for y in range(n))

