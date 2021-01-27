'''
brute force O(n^m)
dp bit mask O(m 2^n)
hungarain / KM / min cost max flow O(poly)
'''

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # O(N^M*2^M) => O(NM*2^M)
        # dp[i][mask] = represents the state of the first i of group 1 being connected, with mask representing which nodes of group 2 have been covered already by previous steps in the DFS
        # There are basically two steps:
        # 1. Connect all group1 nodes to group2. Each group1 node only sends out 1 edge.
        # 2. For all the unconnected nodes in group2, connect them with their min-cost counterparty in group1.
        # We use DP + Bitmask to achieve this. The step 1 above is the DP transition step and the step 2 above is the DP base case.
        m, n = len(cost), len(cost[0])
        min_arr = [min(x) for x in zip(*cost)] # get min value for each row
        
        @lru_cache(None)
        def dp(i, mask):
            if i == m: # base case, i to the end
                ans = 0
                for j in range(n):
                    if not mask & (1 << j): # if j not connected
                        ans += min_arr[j]
                return ans
            
            ans = float('inf')
            for j in range(n): # try all j for each i
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return ans
        
        return dp(0, 0)
        