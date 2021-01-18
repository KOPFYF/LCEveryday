# Template 1. topo sort using BFS
class Solution_bfs:
    def topo_sort_bfs(self, n, prereq):
        # BFS, time O(V + E), space O(V^2)

        # step 1: build graph and init indegree 
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites: # i out & j in
            G[i].append(j)
            degree[j] += 1

        # step 2: bfs, find node with indegree = 0
        bfs = deque([i for i in range(n) if degree[i] == 0])
        res  = []
        while bfs:
            cur = bfs.popleft()
            res.append(cur)
            for nxt in G[cur]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    bfs.append(nxt)
        return res if not sum(degree) else []
        

# Template 2. topo sort using DFS
class Solution_dfs:
    def topo_sort_dfs(self, n, prereq):
        # DFS, time O(V + E), space O(V^2)

        # Step 1: build graph and init visited(3 states) 
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        
        for x, y in prerequisites:
            graph[x].append(y) # trick: reversed the edge direction
        
        # Step 2: run DFS recursively
        ans = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, ans):
                return []
        return ans
    
    def dfs(self, graph, visited, i, ans):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j, ans):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        ans.append(i)
        return True