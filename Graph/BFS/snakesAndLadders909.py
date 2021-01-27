class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def label2pos(label): 
            # mapping label to 2d board pos
            x, y = (label - 1) // n, (label - 1) % n
            if x % 2 == 0:
                return n - x - 1, y
            else:
                return n - x - 1, n - y - 1
        
        seen = set()
        dq = deque([(1, 0)]) # label, step
        while dq:
            label, step = dq.popleft()
            x, y = label2pos(label)
            if board[x][y] != -1: label = board[x][y] # snake/ladder
            if label == n ** 2: return step
                
            for d in range(1, 7):
                nlabel = label + d
                if 0 < nlabel <= n ** 2 and nlabel not in seen:
                    seen.add(nlabel)
                    dq.append((nlabel, step + 1))
        return -1