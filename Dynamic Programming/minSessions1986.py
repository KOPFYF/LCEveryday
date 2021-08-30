class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        '''
        the ith task takes tasks[i] hours to finish
        work for "at most sessionTime" consecutive hours and then take a break
        You may complete the tasks in any order.
        n == tasks.length
        1 <= n <= 14
        1 <= tasks[i] <= 10
        max(tasks[i]) <= sessionTime <= 15
        
        n! = 87,178,291,200 > 10**9
        
        dp: O(2^n * n) / O(2^n)
        we have 2^n masks and O(n) transitions from given mask
        bitmask: full (1 << n) - 1, for example 1111 => 0000
        '''
        n = len(tasks)
        full_mask = (1<<n) - 1
        
        @lru_cache(None)
        def dfs(mask):
            # return the minimum number of work sessions given mask, and current time
            if mask == 0:
                return (1, 0) # (min count, current used time)
                
            res = (float('inf'), float('inf'))
            for i in range(n):
                if mask & (1 << i): # current task not used, try it!
                    cur_cnt, cur_time = dfs(mask ^ (1 << i))
                    full = int((cur_time + tasks[i]) > sessionTime) # flag to tell if full
                    nxt_cnt = cur_cnt + full 
                    nxt_time = tasks[i] + (1 - full) * cur_time # if full, create a new session
                    res = min(res, (nxt_cnt, nxt_time))
            return res
        
        return dfs(full_mask)[0]