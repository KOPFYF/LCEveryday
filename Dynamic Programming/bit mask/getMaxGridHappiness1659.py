class Solution:
    def getMaxGridHappiness(self, m: int, n: int, I: int, E: int) -> int:
        # DFS + Memo, tracking last n cells, O(3^n)
        # For each cell we have 3 states -> 0: empty, 1: intro, 2: extro
        # Only previous N bits matter (previous 1 is left, previous N is up)
        # Naturally, we use Ternary to construct our prevN bit mask
        # There are totally 3^5 = 243 combinations, meaning the prevN value is bounded by 243.
        # For each cell: try all posibilities: 0, 1 or 2
        # 0: do nothing, move our prevN bit mask with new 0 bit.
        # 1: happiness 120, move our prevN bit mask with new 1 bit.
        # 2: happiness 40, move our prevN bit mask with new 2 bit.
        # Check up and left cells to determine how many extra happiness need to be added/subtracted.
        init, gain = [None, 120, 40], [None, -30, 20]
    
        # get the i-th bit, return 0, 1, 2
        get = lambda val, i: (val // (3 ** i)) % 3
        # shift left and set last bit to s
        update = lambda val, s: (val * 3 + s) % (3 ** n)

        @lru_cache(None)
        def dp(x: int, y: int, i: int, e: int, mask: int) -> int:
            if x == n: 
                x, y = 0, y + 1 # shift to next line
            if i + e == 0 or y == m: # till the end
                return 0

            ans = dp(x + 1, y, i, e, update(mask, 0))
            up, left = get(mask, n - 1), get(mask, 0)

            for cur, count in enumerate([i, e], 1):
                if count == 0: continue
                s = init[cur]
                if x - 1 >= 0 and left: s += gain[cur] + gain[left]
                if y - 1 >= 0 and up: s += gain[cur] + gain[up]
                ans = max(ans, s + dp(x + 1, y, 
                                      i - (cur == 1), 
                                      e - (cur == 2),
                                      update(mask, cur)))
            return ans
        return dp(0, 0, I, E, 0)