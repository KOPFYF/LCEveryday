class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """

        n = len(graph)
        out_degree = collections.defaultdict(int) # outdegree for each node
        in_nodes = collections.defaultdict(list) # downstream nodes for each node
        queue = deque([])
        res = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                # collect all terminal nodes into deque
                queue.append(i)
            for j in graph[i]:
                # collect all in nodes
                in_nodes[j].append(i)  
        while queue:
            term_node = queue.popleft()
            res.append(term_node)
            for in_node in in_nodes[term_node]:
                # loop all downstream nodes, topo-sort
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    # find another term_node
                    queue.append(in_node)
        return sorted(res)


class Solution2(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # Same as course schedule II
        # detect a cycle, 0: non-visited, 1: safe(visited), 2:unsafe(visiting)
        # Time complexity: O(V+E)
        # Space complexity: O(V+E)
        n = len(graph)
        color = [0] * n
        res = []
        for i in range(n):
            if self.dfs(graph, i, color):
                res.append(i)
        return res

    def dfs(self, graph, start, color):
        # return True if no cycle detected
        if color[start] == 2:
            # found a cycle
            return False
        elif color[start] == 1:
            # visited, no cycle
            return True
        color[start] = 2
        for end in graph[start]:
            if not self.dfs(graph, end, color):
                return False
        color[start] = 1
        return True