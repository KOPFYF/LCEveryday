class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        free = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '#':
                    continue
                if grid[x][y] == "T":
                    target = (x, y)
                if grid[x][y] == "B":
                    bx, by = (x, y)
                if grid[x][y] == "S":
                    sx, sy = (x, y)
                free.add((x, y))
        
        visited = set()
        heap = [(0, sx, sy, bx, by)]
        while heap:
            moves, sx, sy, bx, by = heapq.heappop(heap)
            if (bx, by) == target:
                return moves
            if (sx, sy, bx, by) in visited:
                continue
            visited.add((sx, sy, bx, by))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = sx + dx, sy + dy
                if (nx, ny) == (bx, by) and (bx + dx, by + dy) in free and (nx, ny, bx + dx, by + dy) not in visited:
                    # push the box one step ahead
                    heapq.heappush(heap, (moves + 1, nx, ny, bx + dx, by + dy))
                elif (nx, ny) in free and (nx, ny) != (bx, by) and (nx, ny, bx, by) not in visited:
                    # no push, just free running, box stay the same place
                    heapq.heappush(heap, (moves, nx, ny, bx, by))
        return -1


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        # First define a function to check from current state, what are the possible neighbouring states (use BFS to check if we can move the player to required location). Notice that the state includes both the location of the box and the player.
        # Second BFS to see if we can reach the target location.
        # this loop is to get the coordinates of target, box and person. Nothing else is gained here
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "T":
                    target = (i,j)
                if grid[i][j] == "B":
                    box = (i,j)
                if grid[i][j] == "S":
                    person = (i,j)

        # this function checks whether the given coordinates/indices are valid to go
        def valid(x,y):
            return 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]!='#'

        # this function checks whether the person can travel from current postition to destination position.
        # used simple bfs(dfs can also be used here), should be self explainatory if you know BFS.
        def check(curr, dest, box):
            que = deque([curr])
            v = set()
            while que:
                pos = que.popleft()
                if pos == dest: return True
                new_pos = [(pos[0]+1,pos[1]),(pos[0]-1,pos[1]),(pos[0],pos[1]+1),(pos[0],pos[1]-1)]
                for x,y in new_pos:
                    if valid(x,y) and (x,y) not in v and (x,y)!=box:
                        v.add((x,y))
                        que.append((x,y))
            return False

        q = deque([(0, box, person)])
        vis = {box + person}
        # this is the main bfs which gives us the answer
        while q :
            dist, box, person = q.popleft()
            if box == target: # return the distance if box is at the target
                return dist

            #these are the new possible coordinates/indices box can be placed in (up, down, right, left).
            b_coord = [(box[0]+1,box[1]),(box[0]-1,box[1]),(box[0],box[1]+1),(box[0],box[1]-1)]
            #these are the corresponding coordinates the person has to be in to push .. the box into the new coordinates
            p_coord = [(box[0]-1,box[1]),(box[0]+1,box[1]),(box[0],box[1]-1),(box[0],box[1]+1)]

            for new_box, new_person in zip(b_coord,p_coord): 
                # we check if the new box coordinates are valid and our current state is not in vis
                if valid(*new_box) and new_box+box not in vis:
                    # we check corresponding person coordinates are valid and if it is possible for the person to reach the new coordinates
                    if valid(*new_person) and check(person,new_person,box):
                        vis.add(new_box+box)
                        q.append((dist+1,new_box,box))

        return -1