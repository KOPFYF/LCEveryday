class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        '''
        dp(i, k): minimum arriving time
        i is # of roads we traversed, k is # of skips
        '''
        n, s = len(dist), sum(dist)
        if s > speed * hoursBefore:
            return -1
        
        @lru_cache(None)
        def dfs(i, k):
            if k < 0: # out of skips
                return float('inf')
            if i < 0: # spend 0 time traverse 0 stops
                return 0
            # two options, skip and use k, or no skip
            # return dist[i] + min(dfs(i-1, k-1), (dfs(i-1, k) + speed - 1)//speed*speed)
        
            no_skip = (dfs(i - 1, k) + speed - 1) // speed * speed # no skip
            skip = dfs(i - 1, k - 1)
            return dist[i] + min(skip, no_skip)

    
        for k in range(n + 1):
            if dfs(n - 1, k) <= speed * hoursBefore:
                return k