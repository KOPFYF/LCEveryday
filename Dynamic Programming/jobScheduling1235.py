class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Top down DP + binary search
        start, end, profit = zip(*sorted(zip(startTime, endTime, profit)))
        # print(start, end, profit)
        # insert end_i into start, from right to left
        jump = {i: bisect_left(start, end[i]) for i in range(len(start))}
        
        @cache
        def dfs(i):
            # subproblem is dfs(jump[i])
            if i == len(start):
                return 0
            # dont use event_i, or use event_i and jump
            return max(dfs(i+1), dfs(jump[i]) + profit[i])
        
        return dfs(0)


class Solution1:
    def jobScheduling2(self, start: List[int], end: List[int], profit: List[int]) -> int:

        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)}

        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            dp[i] = max(dp[i+1], profit[i] + dp[jump[i]])

        return dp[0]



class Solution2(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # DP[j] = max(vj + DP[p(j)], DP[j-1])
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]] # [end, current profit] at time 0 profit is zero
        for s, e, p in jobs:
            # find the index i < j such that job i is compatible with j's start time
            # be careful of +1/-1, s+1 because bisect left to find job end <= s, 
            # -1 because we have a [0, 0]
            # bisect.bisect(dp, [s + 1]) is equals to bisect.bisect(dp, [s + 1, float('-inf')]).
            i = bisect.bisect_left(dp, [s + 1]) - 1
            
            # case 1: don't do this job  -> nothing changes, dp[end_time] = dp[previous end_time]
            # case 2: do this job -> dp[end_time] = dp[previous end_time <= s that gives max profit] + p
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]