'''
For each direction:
Check if any of the neighbors is empty, if yes, break; 
otherwise, keep checking till encounter a cell of same color, return true if size no less than 3, otherwise break.

'''

class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                size = 2 # count source node and first move
                nx, ny = dx + rMove, dy + cMove
                while 0 <= nx < 8 and 0 <= ny < 8:
                    if board[nx][ny] == '.':
                        break
                    elif size < 3 and board[nx][ny] == color: # size = 2 and same color
                        break
                    elif board[nx][ny] == color:
                        return True
                    else: # keep searching
                        nx += dx
                        ny += dy
                        size += 1
        return False