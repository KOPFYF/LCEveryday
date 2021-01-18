class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS, O(4 ^ 10 + 4 * 10)
        deadSet = set(deadends)
        bfs = collections.deque([('0000', 0)])
        seen = set(['0000'])
        
        while bfs:
            cur, step = bfs.popleft()
            if cur == target: return step
            if cur in deadSet: continue # skip current loop
            # nxt node has 4 * 2 possible cases
            for i in range(4):
                digit = int(cur[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10 # (9 + 1) % 10 = 0
                    nxt = cur[:i] + str(new_digit) + cur[i+1:]
                    if nxt not in seen:
                        bfs.append((nxt, step + 1))
                        seen.add(nxt)
        return -1