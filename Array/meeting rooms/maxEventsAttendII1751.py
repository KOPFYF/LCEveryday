'''
Sort the events with respect to starting time. If you attend the current event then binary search the first event which you could attend after this. If you don't attend the current event, then just check the next one after

bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. bisect.bisect_right returns the rightmost place in the sorted list to insert the given element.

An alternative question is when are they equivalent? By answering this, the answer to your question becomes clear.

They are equivalent when the the element to be inserted is not present in the list. Hence, they are not equivalent when the element to be inserted is in the list.
'''
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # dp
        events.sort()
        starts = [s[0] for s in events]
        
        @lru_cache(None)
        def dfs(i, k):
            if k == 0 or i >= len(events):
                return 0
            
            j = bisect.bisect_right(starts, events[i][1])
            # skip current event, or attend, and put pointer to j(next avaible event)
            return max(dfs(i+1, k), events[i][-1] + dfs(j, k-1))
        
        return dfs(0, k)