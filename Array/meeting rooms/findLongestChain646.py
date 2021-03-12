class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # exactly the same as 452
        pairs.sort(key=lambda x:x[1])
        cnt = 0
        end = float('-inf')
        for s, e in pairs:
            if s > end:
                end = e
                cnt += 1
        return cnt