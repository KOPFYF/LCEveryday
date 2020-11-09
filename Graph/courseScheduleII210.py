class Solution1(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # BFS, time O(V + E), space O(V^2)
        n = numCourses
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites: # i out & j in
            G[i].append(j)
            degree[j] += 1
        bfs = deque([i for i in range(n) if degree[i] == 0])
        res  = []
        while bfs:
            cur = bfs.popleft()
            res.append(cur)
            for nxt in G[cur]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    bfs.append(nxt)
        if not sum(degree):
            return res
        else:
            return []

'''
When building the graph, in 207, it does not matter if (x,y) is x->y or y->x, 
cause we only care about the cycle and return Boolean. 
However, in 210, we need to be careful about the direction of the edge. 
If we use graph[y].append(x), we need to return the reversed topological list. 
Think of it like a LIFO stack. If we build the graph like graph[x].append(y), no need to reverse the list. 
一种build graph比较直观, 但是多了一步reverse，第二种比较偷懒，但解释起来复杂一点
'''
class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # DFS
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        # create graph
        for x, y in prerequisites:
            graph[x].append(y)
        # visit each node
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