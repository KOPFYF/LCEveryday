'''
% means empty cell and * means points in blocked
% % % % % *
% % % % *
% % % *
% % *
x *
*
the max bfs step may like this:
4 5 6 7 8 *
3 % % % *
2 % % *
1 % *
x *
*
so the maxstep should be len(blocked)*2
'''

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # Time complexity depends on the size of blocked
        # The maximum area blocked are B * (B - 1) / 2.
        # As a result, time and space complexity are both O(B^2)
        # In my solution I used a fixed upper bound 20000.
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                # BFS in 4 directions need block.length * 2 as step bounds,
                # BFS in 8 directions need block.length as step bounds.
                # Simple search will get TLE, because the big search space
                if len(bfs) == 20000: return True 
            return False
        # starting from a point, you can walk for 20000 steps does not mean the other point is within reach. It only mean your start point is not bounded by the block point.
        return bfs(source, target) and bfs(target, source)