class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True

        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r - l) // 2
            if check(m): # means we can ship within weight=m, search [l, m)
                r = m
            else:
                l = m + 1
        return l