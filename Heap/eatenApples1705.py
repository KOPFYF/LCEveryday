class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # greedy, eat apples that will rot first
        # heap sorted by finished time
        res = i = 0
        hq = []
        while i < len(apples) or hq:
            if i < len(apples) and apples[i] > 0:
                heapq.heappush(hq, [i + days[i], apples[i]])
            while hq and (hq[0][0] <= i or hq[0][1] == 0):
                # if rot or apples[i] are all eaten, delete
                heapq.heappop(hq)
            if hq:
                hq[0][1] -= 1
                res += 1 # eat one
            i += 1
        return res