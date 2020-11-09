class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # time O(nlogn), space O(n)
        graph = collections.defaultdict(list)
        for src, des in tickets:
            graph[src].append(des)
        for k in graph:
            graph[k].sort(reverse=True) # pop last element 
        
        stack = []
        res = []
        stack.append('JFK')
        
        while stack:
            nxt = stack[-1]
            if nxt in graph and len(graph[nxt]) > 0:
                # nxt has child, greedy search
                stack.append(graph[nxt].pop())
            else: 
                # nxt does not have children, out-degree = 0
                res.append(stack.pop())
        # since it's stack, return reversed list
        return res[::-1]