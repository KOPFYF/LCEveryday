class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) >= 2:
            s1 = heapq.heappop(sticks)
            s2 = heapq.heappop(sticks)
            s = s1 + s2
            res += s
            heapq.heappush(sticks, s)
        
        return res 