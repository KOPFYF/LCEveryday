'''
The maximum result happens when in a path from 0 to target, all the intermediate nodes (excluding 0 and target) have an additional self-edge. e.g.

red_edges = [[0, 1], [1, 2], [2, 3]]
blue_edges = [[1, 1], [2, 2]]
n = 4

The minimum step to reach 3 is 5 steps, because all intermediate nodes 1 and 2 contain self-edges. In other words, the maximum result can be 2 * (n - 2) + 1.
'''

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # BFS
        # the maximum result can be n * 2 - 3
        M = 2 * n # max
        graph = [[[], []] for _ in range(n)]
        for i, j in red_edges: graph[i][0].append(j)
        for i, j in blue_edges: graph[i][1].append(j)
        bfs = [[0, 0], [0, 1]] # node, color
        res = [[0, 0]] + [[M, M] for _ in range(n-1)]
        while bfs:
            nxt_bfs = []
            for u, c in bfs:
                for v in graph[u][c]:
                    if res[v][c] == M: # unvisited
                        res[v][c] = res[u][1 - c] + 1
                        nxt_bfs.append([v, 1 - c]) # flip the color
            bfs = nxt_bfs

        return [x if x < M else -1 for x in map(min, res)]

