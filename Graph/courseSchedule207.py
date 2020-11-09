class Solution1(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # BFS, time O(V + E), space O(V^2)
        G = [[] for i in range(n)]
        degree = [0] * n # indegree list
        for j, i in prerequisites: # i out & j in
            G[i].append(j)
            degree[j] += 1 # count the indegrees
        # BFS starts from nodes with indegree == 0
        bfs = deque([i for i in range(n) if degree[i] == 0])
        while bfs:
            cur = bfs.popleft()
            for nxt in G[cur]:
                degree[nxt] -= 1 # remove current node will dec the indegree of next node
                if degree[nxt] == 0: # find another sink and append to deque
                    bfs.append(nxt)
        # in the end if there is still some node has indegree, return false
        return not sum(degree)


class Solution2(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # DFS, time O(V + E), space O(V^2)
        graph = [[] for i in range(n)]
        status = [0] * n
        for x, y in prerequisites:
            graph[y].append(x)
            
        # 0 unvisited, 1 visiting, 2 visited
        # instead of regular DFS with only 2 status, visited/unvisited, 
        # topological sort by detecting a cycle needs a 3rd status, visiting
        for i in range(n):
            # if status[i] == 0:
            # if not visited, run DFS
            if self.dfs(i, status, graph):
                return False
        return True
        
    def dfs(self, node, status, graph):
        # return True if we find a cycle
        if status[node] == 2:
            # if current node is visited, return no cycle
            return False
        elif status[node] == 1:
            # if node is visiting, we find a cycle! 
            return True
        status[node] = 1
        for c in graph[node]:
            if self.dfs(c, status, graph):
                return True
        status[node] = 2
        return False