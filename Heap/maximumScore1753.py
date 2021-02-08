class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        hq = [(-a, 0), (-b, 1), (-c, 2)]
        heapq.heapify(hq)
        step = 0
        
        while hq:
            # print(hq)
            max1, idx1 =  heapq.heappop(hq)
            max2, idx2 =  heapq.heappop(hq)
            
            if max1 < 0 and max2 < 0:
                heapq.heappush(hq, (max1 + 1, idx1)) 
                heapq.heappush(hq, (max2 + 1, idx2))
                step += 1
            else:
                return step