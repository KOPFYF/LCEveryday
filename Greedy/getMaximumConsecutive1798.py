'''
if we reached number i, that means that we can make all numbers 0...i. So, if we add a coin with value 5, we can also make numbers 8..12 (i + 5).
'''

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # greedy
        coins.sort()
        max_val = 0
        for coin in coins:
            if coin > max_val + 1:
                break
            max_val += coin
        return max_val + 1