class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(m):
            i, j = 0, 0
            remove = set(removable[:m])
            while i < len(s) and j < len(p):
                if i in remove: # can be removed from s
                    i += 1
                    continue
                if s[i] == p[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == len(p)
        
        l, r = 0, len(removable)  # have to + 1, because we output l - 1
        while l < r:
            mid = (l + r) // 2
            # print(l, r, mid, check(mid))
            if check(mid):
                # we can use first m chars to remove and still get the subseq
                l = mid + 1
            else:
                r = mid
        return l - 1