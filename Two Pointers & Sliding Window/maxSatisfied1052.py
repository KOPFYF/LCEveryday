class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # time O(n), space O(1)
        satisfied, unsatisfied, trickSatisfied = 0, 0, 0
        for i, c in enumerate(customers):
            if not grumpy[i]:
                satisfied += c
            else:
                unsatisfied += c
            if i >= X: # shrink the window
                unsatisfied -= customers[i - X] * grumpy[i - X] # we can turn this into trickSatisfied
            
            trickSatisfied = max(trickSatisfied, unsatisfied)
        
        return satisfied + trickSatisfied
