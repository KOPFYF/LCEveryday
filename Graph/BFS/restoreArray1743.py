class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        indegree = defaultdict(int)
        graph = defaultdict(set)
        for u, v in adjacentPairs:
            indegree[u] += 1
            indegree[v] += 1
            graph[u].add(v)
            graph[v].add(u)
        
        # print(indegree)
        for u, degree in indegree.items():
            if degree == 1:
                bfs = deque([u])
                seen = set([u])
                break
        
        res = []
        while bfs:
            u = bfs.popleft()
            res.append(u)
            for v in graph[u]:
                if v not in seen:
                    bfs.append(v)
                    seen.add(v)
        return res