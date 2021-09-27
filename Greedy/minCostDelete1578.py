class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        # most easy to understand
        # we need cost = sum_cost(group) - max_cost(group)
        s += '#'
        cost += [0]
        n = len(s)
        res, max_cost, sum_cost = 0, 0, 0
        for i in range(n):
            if i > 0 and s[i] != s[i - 1]:
                # cal and reset when switch groups
                res += sum_cost - max_cost
                max_cost, sum_cost = 0, 0
            sum_cost += cost[i]
            max_cost = max(max_cost, cost[i])
        
        # res += sum_cost - max_cost
        return res

        
class Solution1(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        # greedy O(n)/O(1)
        # For each group of continuous same characters,
        # we need cost = sum_cost(group) - max_cost(group)
        n = len(s)
        res, max_cost = 0, 0
        
        for i in range(n):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i]) # add all cost except the max_cost
            max_cost = max(max_cost, cost[i])
        return res
        
        

class Solution2:
    def minCost(self, s: str, cost: List[int]) -> int:
        # greedy, 2 pointers
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