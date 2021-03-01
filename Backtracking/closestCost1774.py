class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        # soln1, backtracking + pruning
        toppingCosts.sort()
        self.res, n = float(inf), len(toppingCosts)
        def helper(i, sofar):
            if abs(sofar-target) < abs(self.res-target):
                self.res = sofar
            if i < n and sofar < target: # pruning
                helper(i+1, sofar)
                helper(i+1, sofar+toppingCosts[i])
                helper(i+1, sofar+toppingCosts[i]*2)
        for baseCost in baseCosts:
            helper(0, baseCost)
        return self.res
    
        # soln2, backtracking  
        def dfs(cost, i):
            res.append(cost)
            for j in range(i, len(toppingCosts)):
                dfs(cost + toppingCosts[j], j + 1)
                dfs(cost + toppingCosts[j] * 2, j + 1)
        res = []
        for base in baseCosts:
            dfs(base, 0)
        return min(res, key = lambda x: (abs(target - x), x))
    
        # soln3, combination, slowest
        tops = 2*toppingCosts
        k = len(tops)
        sums = set()
        for base in baseCosts:
            for i in range(k + 1):
                combs = combinations(tops, i)
                for comb in combs:
                    sum_ = 0
                    for item in comb:
                        sum_ += item
                    sums.add(sum_ + base)
            
        res = []
        for s in sums:
            res.append((abs(target - s), s))
        res.sort()
        
        return res[0][1]


        
        
        