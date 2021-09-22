class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # scan by start/end time, dp to keep max value
        rideVals = collections.defaultdict(list)
        for s, e, t in rides:
            rideVals[e].append([s, e - s + t]) # key: e, value: [s, benefit]
            
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] # do not pick up passanger i
            for s, t in rideVals[i]:
                # for the same end time at i, call dp[s] and check all possible
                dp[i] = max(dp[i], t + dp[s])
        return dp[-1]
    
    
        rideStartAt = defaultdict(list)
        for s, e, t in rides:
            rideStartAt[s].append([e, e - s + t])  # [end, dollar]

        dp = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            for e, d in rideStartAt[i]:
                dp[i] = max(dp[i], dp[e] + d)
            dp[i] = max(dp[i], dp[i + 1])

        return dp[1]