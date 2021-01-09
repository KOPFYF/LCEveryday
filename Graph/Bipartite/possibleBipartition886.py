class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        def dfs(cur, color):
            # return True if we are able to color current node
            colors[cur] = color
            for i in graph[cur]:
                if colors[i] == color: 
                    return False
                if colors[i] == -color:
                    continue
                if colors[i] == 0 and not dfs(i, -color): 
                    return False
            return True
            
        graph = collections.defaultdict(list)
        for i, j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        colors = [0] * N
        for i in range(N):
            # loop each node and color if it's not colorized yet
            if colors[i] == 0 and not dfs(i, 1): 
                # if current node not colorized, and not able to color it
                return False
        return True