class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def check(K):
            # return sum(math.ceil(pile / speed) for pile in piles) <= H  # slower        
            # return sum((pile - 1) // speed + 1 for pile in piles) <= H  # faster
            cnt = 0
            for p in piles:
                cnt += (p - 1) // K + 1
            return cnt <= H
        
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                # he can eat with speed = mid within H hours, current speed is too fast
                r = mid
            else:
                l = mid + 1
        return l