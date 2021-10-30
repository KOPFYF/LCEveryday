class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for s, e in tickets:
            graph[s].append(e)
        for k in graph:
            graph[k].sort(reverse=True)
        # dfs
        path = []
        def dfs(node):
            
            while graph[node]:
                nxt_node = graph[node].pop()
                dfs(nxt_node)
            path.append(node)
            
        dfs('JFK')
        return path[::-1]

        

class Solution0:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
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


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # dfs with stack, time O(nlogn), space O(n)
        graph = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        for k in graph:
            graph[k].sort(reverse=True) # pop last element 
        
        stack = []
        res = []
        stack.append('JFK')
        
        while stack:
            nxt = stack[-1] # best candidate
            if nxt in graph and len(graph[nxt]) > 0:
                # nxt has child, greedy search
                stack.append(graph[nxt].pop())
            else: 
                # nxt does not have children, out-degree = 0
                res.append(stack.pop())
                # print(res)
        # since it's stack, return reversed list
        return res[::-1]
        