class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        https://leetcode.com/problems/minimum-cost-for-tickets/discuss/810749/Python-by-DP-w-Visualization
        1 <= days.length <= 365
        dp[ d ] = min( dp[d - 1] + cost[0],
               dp[ max(d - 7, 0)  ] + cost[1],
			   dp[ max(d - 30, 0) ] + cost[2] )
        '''
        # O(days)
        dp = [0 for _ in range(366)]
        days_set = set(days)
        
        for i in range(1, 366):
            if i not in days_set:
                dp[i] = dp[i - 1] # no need for current day, cost stays the same
            else:
                dp[i] = min(dp[i - 1] + costs[0], \
                           dp[max(i - 7, 0)] + costs[1], \
                           dp[max(i - 30, 0)] + costs[2] )
        # print(dp[:15])
        return dp[-1]


        # https://leetcode.com/problems/minimum-cost-for-tickets/discuss/811521/Python-or-3-lines-intuitive-DP-or-binary-search-or-beats-99
        @lru_cache(None)
        def dfs(i):
            if i >= n: 
                return 0
            return min(costs[0] + dfs(bisect.bisect_left(days, days[i] + 1)), \
                      costs[1] + dfs(bisect.bisect_left(days, days[i] + 7)), \
                      costs[2] + dfs(bisect.bisect_left(days, days[i] + 30)))
        
        n = len(days)
        return dfs(0)
