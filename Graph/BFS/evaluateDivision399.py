class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        n = len(equations)
        for i in range(n):
            u, v = equations[i]
            w = values[i]
            graph[u][v] = w # u / v = w
            graph[v][u] = 1.0 / w
        
        def bfs(query):
            s, e = query
            if s not in graph or e not in graph: 
                return -1.0
            if s == e: 
                return 1.0
            
            bfs, seen = deque([(s, 1.0)]), set([s])
            while bfs:
                u, cur = bfs.popleft()
                if u == e:
                    return cur
                for v, w in graph[u].items():
                    if v not in seen:
                        nxt = cur * w
                        # compress, so use s, not u, given s-u-v, return s-v
                        graph[s][v] = nxt
                        graph[v][s] = 1.0 / nxt
                        seen.add(v)
                        bfs.append((v, nxt))
            return -1.0
        
        res =  [bfs(q) for q in queries]
        # print(graph)
        return res


class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # BFS, time O((V + E)*q)
        # a/b = 2.0, b/c = 3.0
        # a -- 2.0 --> b -- 3.0 --> c
        # c -- 1/3 --> b -- 1/2 --> a
        # compress paths to make it faster (add memo)
        graph = defaultdict(dict) 
        for ([x,y], value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value
            
        def bfs(query):
            s, e = query
            if s not in graph or e not in graph: return -1.0
            if s == e: return 1.0
            
            dq, seen = deque([(s, 1.0)]), {s}
            while dq:
                node, prod = dq.popleft()
                for nxt_node, nxt_edge in graph[node].items():
                    nxt_prod = prod * nxt_edge
                    if nxt_node not in seen:
                        if nxt_node == e: return nxt_prod
                        # compress edge
                        graph[s][nxt_node] = nxt_prod
                        graph[nxt_node][s] = 1 / nxt_prod
                        seen.add(nxt_node)
                        dq.append((nxt_node, nxt_prod))
            return -1.0
        
        return [bfs(query) for query in queries]


