class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Time O(nlog(max(bloomDay))), Space O(1)
        n = len(bloomDay)
        if n < m * k:
            return -1

        def check(day, b, adj):
            # check if it's possible to have b bouquets, with each adj flowers, in that day
            # Time O(n), Space O(1)
            flow, bouq = 0, 0
            for bloom in bloomDay:
                if bloom > day:
                    flow = 0 # reset
                else:
                    flow += 1
                # flow = 0 if bloom > day else flow + 1
                if flow >= adj:
                    flow = 0
                    bouq += 1
                    if bouq == b:
                        return True
            return False

        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if check(mid, m, k):
                # we can make it within mid days
                r = mid
            else:
                l = mid + 1
        return l


        
