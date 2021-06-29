class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        # Let dp[i] be the number of ways to solve the problem for the subtree of node i.
        # dp[i] equals the multiplications of the number of ways to distribute the subtrees of the children of i on the array using combinatorics, multiplied by their dp values.
        mod = 10**9 + 7
        graph = defaultdict(list)
        for i, prev in enumerate(prevRoom):
            graph[prev].append(i) # prev -> i
        
        def dfs(cur):
            if not graph[cur]:
                return 1, 1 # number of different orders, subtree depth
            
            res, l = 1, 0
            for nxt in graph[cur]:
                tmp, r = dfs(nxt)
                # put l items into l+r spots and fill the remaining spots with the other r items
                res = (res * tmp * math.comb(l + r, r)) % mod
                l += r
            return res, l + 1
        
        return dfs(0)[0]
            
        