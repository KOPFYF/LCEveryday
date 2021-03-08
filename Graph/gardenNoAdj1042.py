class Solution0(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # All gardens have at most 3 paths coming into or leaving it
        # It means at least one possible color to choose
        # O(V+E), graph search + greedy + bit mask
        colors = [0] * n # store color plan for node from 1 to n. init with 0
        graph = defaultdict(set)
        for u, v in paths:
            graph[u].add(v)
            graph[v].add(u)
        
        for i in range(1, n + 1):
            mask = 0 # 4 bits mask
            for j in graph[i]:
                mask |= (1 << colors[j - 1]) # mark all neighbors color bit to avoid next
            for c in range(1, 5):
                if not (mask & (1 << c)) and colors[i - 1] == 0: 
                    # uncolored and could be colored with color c
                    colors[i - 1] = c
        return colors


class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # All gardens have at most 3 paths coming into or leaving it
        # It means at least one possible color to choose
        # O(V+E), graph search + greedy + bit mask
        colors = [0] * n # store color plan for node from 1 to n. init with 0
        graph = defaultdict(set)
        for u, v in paths:
            graph[u - 1].add(v - 1)
            graph[v - 1].add(u - 1)
        
        for i in range(n):
            mask = 0 # 4 bits mask
            for j in graph[i]:
                mask |= (1 << colors[j]) # mark all neighbors color bit to avoid next
            for c in range(1, 5):
                if not (mask & (1 << c)) and colors[i] == 0: 
                    # uncolored and could be colored with color c
                    colors[i] = c
        return colors
                    
                    
                 