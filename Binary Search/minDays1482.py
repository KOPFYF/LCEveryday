class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n: return -1
        
        def check(day, b, adj):
            # check if it's possible to have b bouquets, with each adj flowers, in that day
            flow, bouq = 0, 0
            for bloom in bloomDay:
                flow = 0 if bloom > day else flow + 1
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
                # decrease day if valid
                r = mid
            else:
                l = mid + 1
        return l