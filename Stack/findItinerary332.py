class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # stack, dfs in iteration
        graph = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)

        for src in graph:
            graph[src].sort(reverse = True) # pop the smallest one

        stack = ['JFK']
        res = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                res.append(stack.pop())

        return res[::-1]

        # heap + dfs
        graph = defaultdict(list)
        
        for ticket in tickets:
            heapq.heappush(graph[ticket[0]], ticket[1])

        visited = [] 
		
		# reach until the end first, on the way back visit missing places
        def dfs(visited, graph, node):
            while graph[node]:
                neighbour = heapq.heappop(graph[node])
                dfs(visited, graph, neighbour)
            visited.append(node)   
            
        dfs(visited, graph, 'JFK')
            
        return visited[::-1]

            
            