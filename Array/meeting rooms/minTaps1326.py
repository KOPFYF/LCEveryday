class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # same as 1024 video stitching
        clips = []
        for i, r in enumerate(ranges):
            if r:
                clips.append([max(0, i - r), i + r])
        clips.sort()
        cnt, end1, end2 = 0, -1, 0
        for s, e in clips:
            if end2 >= n or s > end2: 
                # current end2 loop over or current start has a gap
                break
            if end1 < s <= end2:
                end1 = end2
                cnt += 1
            end2 = max(end2, e)
        return cnt if end2 >= n else -1