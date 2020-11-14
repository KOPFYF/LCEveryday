class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = len(s1)
        n = len(s2)
        if need > n: return False
        d1 = collections.Counter(s1)
        
        d2 = collections.Counter(s2[:need])
        i = 0
        while i + need < n:
            # take substring s2[i: i + need]
            if d1 == d2:
                return True
            d2[s2[i]] -= 1
            if not d2[s2[i]]: # if freq = 0, pop out
                del d2[s2[i]]
            d2[s2[i + need]] += 1
            i += 1
        return d1 == d2 # deal with last case