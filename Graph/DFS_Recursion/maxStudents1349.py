class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        # O(mn) nodes, with each dfs O(mn), so time O(m^2 n^2)
        # seats on even columns and seats on odd columns form a bipartite graph
        # so the maximum independent set on the bipartite graph is the solution
        # https://ali-ibrahim137.github.io/competitive/programming/2020/01/02/maximum-independent-set-in-bipartite-graphs.html
        # In any bipartite graph, #edges in a Maximum matching = #vertices in a minimum vertex cover.
        m, n = len(seats), len(seats[0])
        graph = [[(-1, -1)] * n for _ in range(m)] # store the last position he could spy
        
        def dfs(node, seen):
            # given a node/seat (x, y), could someone spy on him? connect them in a group
            x, y = node
            # assume a virtual edge connecting students who can spy, 6 directions
            dirs = [(-1, -1), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1)]
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not seen[nx][ny] and seats[nx][ny] == '.':
                    # find a bipartite edge and color it as seen
                    seen[nx][ny] = 1
                    if graph[nx][ny] == (-1, -1) or dfs(graph[nx][ny], seen):
                        # update spy if not spied yet, or recursively
                        graph[nx][ny] = (x, y)
                        return True
            return False
        
        res = 0
        for j in range(0, n, 2):
            # loop odd columns
            for i in range(m):
                if seats[i][j] == '.':
                    # for each seat, run dfs and find independent set, update graph
                    seen = [[0] * n for _ in range(m)]
                    if dfs((i, j), seen):
                        # find an cluster
                        res += 1
        
        cnt = sum(1 for i in range(m) for j in range(n) if seats[i][j] == '.')
        
        # The complement of a minimum vertex cover in any graph is the maximum independent set.
        return cnt - res