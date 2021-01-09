class Solution1(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # a/b = 2.0, b/c = 3.0
        # a -- 2.0 --> b -- 3.0 --> c
        # c -- 1/3 --> b -- 1/2 --> a
        # compress paths to make it faster (add memo)
        # build graph takes O(E), each query takes O(N), space takes O(E)
        
        graph = {}
        
        def build_graph(equations, values):
            def add_edge(f, t, value): # (a, b, 2)
                if f in graph:
                    graph[f].append((t, value))
                else:
                    graph[f] = [(t, value)]
                
            for vs, value in zip(equations, values):
                # build bi-directional graph
                f, t = vs
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)
        
        def find_path(query):
            u, v = query
            if u not in graph or v not in graph:
                return -1.0
            
            q = deque([(u, 1.0)]) # (vertex, current product)
            seen = set()
            # BFS
            while q:
                cur_node, cur_prod = q.popleft()
                if cur_node == v:
                    return cur_prod
                seen.add(cur_node)
                for nxt_node, nxt_value in graph[cur_node]:
                    if nxt_node not in seen:
                        q.append((nxt_node, cur_prod * nxt_value))
            
            return -1.0
        
        build_graph(equations, values)
        # print(graph)
        return [find_path(query) for query in queries]


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


