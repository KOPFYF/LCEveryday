class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:       
        items.sort() # sort by price
        n = len(items)
        maxBeautys = [items[0][1]] * n
        for i in range(1, n):
            maxBeautys[i] = max(maxBeautys[i-1], items[i][1])
        # print(items, maxBeautys)
        prices = [x[0] for x in items]
        
        res = []
        for q in queries:
            if items[0][0] > q:
                res.append(0)
            else:
                i = bisect_right(prices, q)
                res.append(maxBeautys[i-1])
        return res