class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # BFS
        stack = [0]
        visit = set(stack)
        
        while stack:
            room = stack.pop()
            for neighbor in rooms[room]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    stack.append(neighbor)
        
        return len(visit) == len(rooms)


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # DFS
        n = len(rooms)
        status = [False] * n
        
        def dfs(rooms, cur, status):
            status[cur] = True # marked as visited
            for nxt in rooms[cur]:
                if not status[nxt]:
                    dfs(rooms, nxt, status)
        dfs(rooms, 0, status)
        return all(status)