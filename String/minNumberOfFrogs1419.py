class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # the number of "c", "r", "o", "a", "k" must be monotonically increasing
        # watermark is the the number of required Frogs
        watermark = c = r = o = a = k = 0
        for ch in croakOfFrogs:
            if ch == 'c': 
                c += 1
                watermark = max(watermark, c - k)
            elif ch == 'r': r += 1
            elif ch == 'o': o += 1
            elif ch == 'a': a += 1
            else: k += 1
            if not c >= r >= o >= a >= k:
                return -1
            # print(watermark, c, k)
        return watermark if c == k else -1