class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        # slice into m subarrays with limit width, min(sum of height)
        
        # dp[i] minimum height for books[:i], O(n^2)
        # dp[i] = dp[j] + books[j:i]
        n = len(books) 
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0
        
        for i in range(1, n + 1):
            w, h = books[i - 1][0], books[i - 1][1]
            dp[i] = dp[i - 1] + h # init
            for j in range(i - 1, 0, -1):
                if w + books[j - 1][0] <= shelf_width:
                    h = max(h, books[j - 1][1])
                    w += books[j - 1][0]
                    dp[i] = min(dp[i], dp[j - 1] + h)
                else:
                    break
        
        return dp[-1]
        
        
        # dp[i] minimum height for books[i:], O(n^2)
        @lru_cache(None)
        def dfs(pos):
            if pos == len(books):
                return 0
            width, res, maxh = 0, float('inf'), 0
            
            # check books[pos: i], and call dfs(i + 1), which is books[i+1:]
            # so dfs(pos) = books[pos: i] & dfs(i + 1)
            for i in range(pos, len(books)):
                if width + books[i][0] <= shelf_width:
                    width += books[i][0]
                    maxh = max(maxh, books[i][1])
                    res = min(res, maxh + dfs(i + 1))
                else:
                    break
            return res
        
        return dfs(0)
        
        