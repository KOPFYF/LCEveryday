class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(cell) for row in board for cell in row)
        bfs, seen = deque([(s, s.index('0'), 0)]), {s}
        
        m, n = len(board), len(board[0])
        while bfs:
            encoding, index0, steps = bfs.popleft()
            if encoding == '123450':
                return steps
            x, y = index0 // n, index0 % n
            # try to switch 0 with neighbors
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    flatten = [digit for digit in encoding]
                    flatten[index0], flatten[nx*n+ny] = flatten[nx*n+ny], flatten[index0]
                    nxt_encoding = ''.join(flatten)
                    if nxt_encoding not in seen:
                        seen.add(nxt_encoding)
                        bfs.append((nxt_encoding, nx*n+ny, steps + 1))
        
        return -1

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # BFS, where the nodes are the puzzle boards 
        # and edges are if two puzzle boards can be transformed into one another with one move.
        s = ''.join(str(d) for row in board for d in row) # Encode board permutation
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index('0')))
        steps, height, width = 0, len(board), len(board[0]) 
        while dq:
            for _ in range(len(dq)):
                t, i = dq.popleft() # t is encoding, i is index of 0
                if t == '123450': # find target
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t] # expand to a list and swap
                        # r * width + c is the string index of board[r][c].
                        # swap '0'(x, y)/(i) and its neighbor.(r, c)/(r * width + c)
                        ch[i], ch[r * width + c] = ch[r * width + c], '0' 
                        s = ''.join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
            steps += 1              
        return -1


class Solution2:
    def slidingPuzzle(self, board):
        # BFS, move dict
        moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]
        while q:
            new = []
            for s, i in q:
                used.add(s)
                if s == "123450":
                    return cnt
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            cnt += 1
            q = new
        return -1