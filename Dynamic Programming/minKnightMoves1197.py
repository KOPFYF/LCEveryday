'''
The moment you reach 0,2 or 2,0 or 1,1 (visualize in the real chess board) the knight cannot move further to 0,0 or might go into negative axis, the smartest way is to if you are in (0,2) move the night to (2,1) then from there it could move to (0,0)..this takes 2 move. same applies for (1,1) and (2,0) too..
'''

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None) 
        def dfs(x, y):
            if x + y == 0:
                return 0
            elif x + y == 3 and x in (1, 2):
                return 1
            elif x + y == 2:
                return 2
            return min(dfs(abs(x-1), abs(y-2)), dfs(abs(x-2), abs(y-1))) + 1
        return dfs(abs(x), abs(y))