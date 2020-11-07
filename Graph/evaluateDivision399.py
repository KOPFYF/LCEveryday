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
    def calcEquation(self, equations, values, queries):
        # build graph takes O(E), each query takes O(N), space takes O(N^2)
        graph = defaultdict(dict) # for compression and memory
        for ([x,y], value) in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value
        
        def find_prod(s,e):
            if s not in graph or e not in graph:
                return -1.0
            if s == e: return 1.0
            q = deque([(s, 1.0)])
            visited = {s}
            while q:
                n, curr = q.popleft()
                for child, value in graph[n].items():
                    if child in visited:
                        continue
                    nc = curr * value
                    if child == e:
                        return nc
                    # compress
                    graph[s][child] = nc 
                    graph[child][s] = 1 / nc
                    visited.add(child)
                    q.append((child, nc))
            return -1.0
        
        return [find_prod(s,e) for [s,e] in queries]


