class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        pre_satisfied = sum(c for c, g in zip(customers, grumpy) if not g)
        n = len(customers)
        res = runsum = sum(c for c, g in zip(customers[:x], grumpy[:x]) if g)
        
        for i in range(n):
            if i + x < n:
                runsum = runsum - customers[i] * grumpy[i] + customers[i+x] * grumpy[i+x]
                res = max(runsum, res)
        return res + pre_satisfied