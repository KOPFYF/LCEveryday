class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        # BFS
        d = defaultdict(list)
        for employee, boss in enumerate(manager):
            d[boss].append(employee)
            
        bfs = deque([(headID, informTime[headID])])
        res = 0
        while bfs:
            boss, cur_time = bfs.popleft()
            res = max(res, cur_time)
            if boss in d:
                for employee in d[boss]:
                    bfs.append((employee, cur_time + informTime[employee]))
        return res