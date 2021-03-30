class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(set)
        indegrees = {u:0 for u in range(1, n+1)}
        for u, v in relations:
            graph[u].add(v)
            indegrees[v] += 1
        
        bfs = deque([u for u in indegrees if indegrees[u] == 0])
        level = 0
        while bfs:
            level += 1
            nxt_bfs = []
            for _ in range(len(bfs)):
                u = bfs.popleft()
                for v in graph[u]:
                    indegrees[v] -= 1
                    if not indegrees[v]:
                        nxt_bfs.append(v)
            bfs = deque(nxt_bfs)

        if sum(indegrees.values()) == 0:
            return level
        return -1