class Solution(object):
    def updateMatrix(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        visited, q = set(), deque()

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        M[nx][ny] = M[x][y] + 1
                        visited.add((nx, ny))
                        q.append((nx, ny))
        return M