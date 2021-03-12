class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        '''
        0,0 to tree[1]
        tree[1] to tree[2]
        …
        tree[n-1] to tree[n]

        Time complexity: O(m^2n^2)

        Space complexity: O(mn)
        '''

        m, n = len(forest), len(forest[0])
        hq = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        heapq.heapify(hq)
        
        i, j, res = 0, 0, 0
        while hq:
            h, x, y = heapq.heappop(hq)
            step = self.bfs(forest, i, j, x, y)
            if step == -1: return -1
            res += step
            i, j = x, y # new start
            
        return res

    def bfs(self, forest, i, j, x, y):
        m, n = len(forest), len(forest[0])
        dq = deque([(i, j, 0)])
        seen = set((i, j))
        # step = 0
        while dq:
            i, j, step = dq.popleft()
            if i == x and j == y:
                return step
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in seen and forest[nx][ny]:
                    seen.add((nx, ny))
                    dq.append((nx, ny, step + 1))
        return -1