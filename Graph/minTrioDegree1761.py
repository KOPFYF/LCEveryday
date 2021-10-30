class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        res = []
        
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if j in graph[i] and k in graph[i] and k in graph[j]:
                        count = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        res.append(count)

        return min(res) if res else -1