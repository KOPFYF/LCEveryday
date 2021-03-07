"""
1. Find minimal rectangle for printing each color. Its corners for color X can be found as minimal and maximal coordinates of cells with X.
2. Each such rectangular might contain cells with different colors, then those colors have to be printed after current one.
3. Using previous point, build dependency graph between colors.
4. If there are cycles in this graph, then it means that color X has to be printed after Y and Y after X, so it's not possible to print.
"""

class Solution:
    def isPrintable(self, M: List[List[int]]) -> bool:
        # find boundary
        bound = [(61, 61, -1, -1) for _ in range(61)]
        m, n = len(M), len(M[0])
        for i in range(m):
            for j in range(n):
                color = M[i][j]
                a, b, c, d = bound[color]
                bound[color] = (min(a, i), min(b, j), max(c, i), max(d, j))
        
        # build graph
        graph = defaultdict(set)
        indegree = [0] * 61
        for color in range(len(bound)):
            a, b, c, d = bound[color]
            if a < 61:
                for i in range(a, c + 1):
                    for j in range(b, d + 1):
                        if M[i][j] != color and M[i][j] not in graph[color]:
                            graph[color].add(M[i][j]) # M[i][j] is in current rect so it must be printed after
                            indegree[M[i][j]] += 1
        
        # print(graph) # defaultdict(<class 'set'>, {1: {3, 4, 5}, 3: {4}})
        # print(indegree)
        
        # cycle detect / topo-sort
        bfs = deque([i for i in range(61) if indegree[i] == 0])
        while bfs:
            cur = bfs.popleft()
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    bfs.append(nxt)
        
        # print(indegree)
        return sum(indegree) == 0