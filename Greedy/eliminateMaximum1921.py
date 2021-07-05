class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # greedy
        res, t = 0, []
        for s, v in zip(dist, speed):
            t.append(s/v)
        t.sort()
        
        for i in range(len(dist)):
            if t[i] > i:
                res += 1
            else:
                break
        return res