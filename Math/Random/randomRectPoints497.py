import random
import bisect

class Solution:
    # weighted probability

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = []
        cur = 0
        
        for x1, y1, x2, y2 in rects:
            # cur is the run sum of how many points in current rect
            cur += (x2 - x1 + 1) * (y2- y1 + 1) # + 1 bc boundary included
            self.ranges.append(cur)
        

    def pick(self) -> List[int]:
        # pick a rect (since flattened, it's even)
        idx = bisect.bisect(self.ranges, random.random())
        x1, y1, x2, y2 = self.rects[idx] 
        # pick one point from that rect
        return [random.randint(x1, x2), random.randint(y1, y2)]
    
        x1, y1, x2, y2 = random.choices(self.rects, cum_weights=self.ranges)[0]
        return [random.randint(x1, x2), random.randint(y1, y2)] 
    
        n = random.randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]
    
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()