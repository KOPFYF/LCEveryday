class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # monotonic inc stack
        stack = []
        res = prices[:]
        for j, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                i = stack.pop()
                res[i] -= price
            stack.append(j)
        return res