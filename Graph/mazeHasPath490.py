class Solution(object):
    def hasPath(self, M, start, end):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # Time: O(m * n): worst case visit the entire matrix
        # Space: O(m * n): seen Matrix
        m, n = len(M), len(M[0])
        seen = [[False] * n for _ in range(m)]
        seen[start[0]][start[1]] = True
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        dq = deque([start])
        while dq:
            # cur = dq.popleft()
            cur = dq.pop()
            if cur[0] == end[0] and cur[1] == end[1]:
                return True
            for dx, dy in dirs:
                nx, ny = cur[0] + dx, cur[1] + dy
                while 0 <= nx < m and 0 <= ny < n and M[nx][ny] != 1:
                    nx += dx
                    ny += dy
                # backwards one step because we are on the wall now
                nx -= dx
                ny -= dy
                if not seen[nx][ny]:
                    dq.append((nx, ny))
                    seen[nx][ny] = True
        return False
        