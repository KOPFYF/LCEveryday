# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        # DFS to explore and BFS to find the shortest path
        # pure BFS will lead to TLE
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        anti = {"U": "D", "D": "U", "L": "R", "R": "L"}
        seen = {}
        seen[0, 0] = master.isTarget() # start point could be the target
        
        def dfs(x, y):
            for d in dirs:
                dx, dy = dirs[d]
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and master.canMove(d):
                    master.move(d)
                    seen[nx, ny] = master.isTarget()
                    dfs(nx, ny)
                    master.move(anti[d]) 
        dfs(0, 0) # after this, map is built by scanning through all isTarget(), stored in seen
        
        bfs = deque([(0, 0, 0)]) # (x, y, dist)
        seen2 = set()
        while bfs:
            x, y, dist = bfs.popleft()
            if seen[x, y]: return dist
            for d in dirs:
                dx, dy = dirs[d]
                nx, ny = x + dx, y + dy
                if (nx, ny) in seen and (nx, ny) not in seen2:
                    seen2.add((nx, ny))
                    bfs.append((nx, ny, dist+1))
        
        return -1
            
            
        
        
        
        
