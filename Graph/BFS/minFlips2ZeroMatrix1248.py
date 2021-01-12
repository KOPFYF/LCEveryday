class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # BFS, O(m * n * 2 ^ (m * n)) / O(2 ^ (m * n))
        # Convert matrix to int
        # Since m < 3, n < 3 are given as constraints, there are at most 9 cells and an int has enough bits to store their values;
        # Map the m * n cells of the initial state of the matrix to the 0 ~ m * n - 1th bits of an int: start;
        # For each one of the m * n bits, flip it and its neighbors, then BFS to check if 0, corresponding to an all 0s matrix, is among the resulting states; if yes, return the minimum steps needed;
        # Use a Set to avoid duplicates;
        # If after the traversal of all states without finding 0, return -1.
        m, n = len(mat), len(mat[0])
        start = sum(cell << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        dq = collections.deque([(start, 0)])
        seen = {start}
        while dq:
            cur, step = dq.popleft()
            if not cur:
                return step
            for i in range(m):
                for j in range(n):
                    nxt = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            # Use next ^ 1 << k (where k = i * n + j) to flip kth bit of next
                            nxt ^= 1 << (r * n + c) 
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, step + 1))
        return -1