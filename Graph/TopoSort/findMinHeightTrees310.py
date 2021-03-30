class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # multi-end bfs/topo sort
        if n == 1: return [0]
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            indegree[u] += 1
            indegree[v] += 1
        
        bfs = [u for u in range(n) if indegree[u] == 1]
        while True:
            nxt_bfs = []
            for u in bfs:
                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 1: # not == 0 !
                        # print(v)
                        nxt_bfs.append(v)
                indegree[u] = 0 # set parent node to 0
            if not nxt_bfs:
                break
            bfs = nxt_bfs
        return bfs


class Solution1(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        G = defaultdict(set)       
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
            
        # multi-end BFS, start from leaves
        dq = deque([v for v in range(n) if len(G[v]) == 1])
        # print(dq)
        while n > 2:
            # remove all leaves
            n -= len(dq)
            for _ in range(len(dq)):
                l = dq.popleft() # this leaf only has one neighbor
                v = G[l].pop() # get that neighbor
                G[v].remove(l) # remove leave from that neighbor
                if len(G[v]) == 1:
                    # new leaf
                    dq.append(v)
        return list(dq)