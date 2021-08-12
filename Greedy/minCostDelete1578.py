class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        res, prev = 0, 0 # prev stores the index of max cost
        for i in range(1, n):
            if s[i] == s[prev]: # find a group
                res += min(cost[prev], cost[i])
                if cost[prev] < cost[i]:
                    prev = i
            else:
                prev = i # thinking of 'abc', prev keeps moving
            
        return res