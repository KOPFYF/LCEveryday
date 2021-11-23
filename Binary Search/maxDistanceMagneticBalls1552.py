class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def check(d):
            cnt, cur = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - cur >= d:
                    cnt += 1
                    cur = position[i]
                    if cnt >= m:
                        return True
            return False
        
        l, r = 0, position[-1] - position[0] + 1
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                # can place m balls with current gap = mid
                l = mid + 1
            else:
                r = mid
        return l - 1