class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # DFS, py nonlocal
        d = defaultdict(list)
        for employee, boss in enumerate(manager):
            d[boss].append(employee)
        res = 0
        
        def dfs(cur_node, cur_time):
            # https://blog.csdn.net/diaoxuesong/article/details/42552943
            nonlocal res
            res = max(res, cur_time)
            for nxt in d[cur_node]:
                dfs(nxt, cur_time + informTime[cur_node])
        dfs(headID, 0)
        
        return res

        # DFS, py self.res
        d = defaultdict(list)
        for employee, boss in enumerate(manager):
            d[boss].append(employee)
        self.res = 0
        
        def dfs(cur_node, cur_time):
            self.res = max(self.res, cur_time)
            for nxt in d[cur_node]:
                dfs(nxt, cur_time + informTime[cur_node])
        dfs(headID, 0)
        
        return self.res
            
        
        # BFS
        d = defaultdict(list)
        for employee, boss in enumerate(manager):
            d[boss].append(employee)
            
        bfs = deque([(headID, informTime[headID])])
        res = 0
        while bfs:
            boss, cur_time = bfs.popleft()
            res = max(res, cur_time) # need to traverse all employers
            if boss in d:
                for employee in d[boss]:
                    bfs.append((employee, cur_time + informTime[employee]))
        return res