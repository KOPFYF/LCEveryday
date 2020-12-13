class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:
        # sort first by increasing width
        # within each subarray of same-width envelopes
        # sort by decreasing height
        envs.sort(key=lambda x: (x[0], -x[1]))
        
        # now find the length of the longest increasing subsequence of heights.
        # Since each same-width block was sorted non-increasing, 
        # we can only pick at most one height within each block
        # otherwise, the sequence would be non-increasing       
        def bs(tails, h):
            # r = len(tails) but not len()-1 becasue len() is also a possible res
            l, r = 0, len(tails)
            while l < r:
                mid = (l + r) // 2
                if tails[mid] >= h:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        tails = []
        for w, h in envs:
            idx = bs(tails, h)
            # idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
        return len(tails)