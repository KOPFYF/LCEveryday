class Solution(object):
    def validTree(self, numCourses, prerequisites):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Number of edges = Number of nodes - 1 and it's acyclic (i.e directed graph with no cycle)
        # Number of edges = Number of nodes - 1 and it's connected (Note: the 1st condition implies that the connected graph has no cycle)
        if len(prerequisites) != numCourses - 1: return False
        G = [[] for _ in range(numCourses)]
        visited = set()
        for post, pre in prerequisites: # undirected graph
            G[post].append(pre)
            G[pre].append(post)
        # BFS
        parent = [-1] * numCourses
        dq = deque([0]) # start with the first node
        while dq:
            cur = dq.popleft()
            visited.add(cur)
            for nxt in G[cur]:
                if nxt not in visited:
                    parent[nxt] = cur
                    dq.append(nxt)
                elif nxt in visited and nxt != parent[cur]:
                    # if a nbr is in visited and the nbr is not the parent, then we have a cycle.
                    return False
        # If the graph is connected then all vertices must be visited
        return len(visited) == numCourses
            
                  
        # DFS
        # Simple extension of cycle finding algorithm for directed graphs. 
        # You need to include the parent as well in the DFS call.
        if self.dfs(0, -1, G, visited):
            return False
        if len(visited) != numCourses:
            # If the graph is connected then all vertices must be visited
            return False
        return True
    
    def dfs(self, node, parent, G, visited):
        # return true if we find a cycle
        visited.add(node)
        for nbr in G[node]:
            if nbr not in visited:
                if self.dfs(nbr, node, G, visited):
                    return True
            elif nbr in visited and nbr != parent:
                # if a nbr is in visited and the nbr is not the parent, then we have a cycle.
                return True
        return False