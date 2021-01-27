class Solution:
    def minRefuelStops(self, target: int, cur: int, stations: List[List[int]]) -> int:
        # Top down DP. 0-1 pack
        n, end = len(stations), target
        memo = {}
        def dfs(cur, pos, target):
            # min res to go further target(remaining) with current fuel as cur
            if cur >= target: return 0 # no need to refuel and success to the end
            if pos == n: return float('inf') # failed to reach the target
            if (cur, pos, target) in memo: return memo[(cur, pos, target)]
            # dis: to go to s[0], we need to burn dis 
            dis, fuel = stations[pos][0] - (end - target), stations[pos][1]
            taken, not_taken = float('inf'), float('inf')
            if cur - dis >= 0: # if stations[pos] is reachable 
                taken = dfs(cur - dis + fuel, pos + 1, end - stations[pos][0]) + 1
                not_taken = dfs(cur - dis, pos + 1, end - stations[pos][0])
                
            memo[(cur, pos, target)] = min(taken, not_taken)
            return memo[(cur, pos, target)]
            
            res = dfs(startFuel, 0, target)
            return res if res != float('inf') else -1