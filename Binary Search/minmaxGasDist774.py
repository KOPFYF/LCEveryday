class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        def check(gap, m):
            # Checking whether it is possible to achieve such distance within m stations
            # return boolean, if we can add m more stations to have a smaller target gap
            cnt = 0
            for a, b in zip(stations, stations[1:]):
                diff = b - a
                cnt += int(diff / gap)
                if cnt > m:
                    return False
            return True
        
        l, r = 1e-6, stations[-1]
        while l + 1e-6 < r:
            mid = (l + r) / 2
            if check(mid, k):
                r = mid
            else:
                l = mid
        return l
                