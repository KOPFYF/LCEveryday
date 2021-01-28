class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # BFS
        M = 2 * n
        graph = [[[], []] for _ in range(n)]
        for i, j in red_edges: graph[i][0].append(j)
        for i, j in blue_edges: graph[i][1].append(j)
        bfs = [[0, 0], [0, 1]]
        res = [[0, 0]] + [[M, M] for _ in range(n-1)]
        while bfs:
            nxt_bfs = []
            for u, c in bfs:
                for v in graph[u][c]:
                    if res[v][c] == M: # unvisited
                        res[v][c] = res[u][1 - c] + 1
                        nxt_bfs.append([v, 1 - c])
            bfs = nxt_bfs

        return [x if x < M else -1 for x in map(min, res)]