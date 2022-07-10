'''
It's a brain-teaser.

res >= max(A)
Because each time,
one type can reduce at most 1 cup,
so the final result is bigger or equal to max(A)

res >= ceil(sum(A) / 2)
Because each time,
we can fill up to 2 cups,
so the final result is bigger or equal to ceil(sum(A) / 2)

The possible strategy is greedily fill up 2 cups with different types of water.
We pick the 2 types with the most number of cups.


Complexity
Time O(n)
Space O(1)

'''

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)