'''
********************** (+1 to count)
                    ******************** (+1)
                 ************************************ (no need to +1 since it overlaps with interval 1)
                                                ********************* (+1 since it started later than the end of the last interval (ie end of interval 2)
                                                       ******** (+1 since it has not finished, end2 >= T, and would need at least one more interval)
                                                                                             ********************** (breaks)
'''
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # DP, take or no take, O(nT)/O(T)
        dp = [float('inf')] * (T + 1)
        dp[0] = 0
        for i in range(T + 1):
            for s, e in clips:
                if s <= i <= end: # overlap
                    dp[i] = min(dp[i], dp[s] + 1) 
                    # dp[s] + 1 means use last res + current clip
        if dp[T] == float('inf'):
            return -1
        return dp[T]
        
        
        
        # greedy O(nlogn)/O(1)
        cnt = 0
        end1, end2 = -1, 0
        # clips.sort(key=lambda x:x[1])
        clips.sort() # sort by start time
        for s, e in clips:
            if end2 >= T or s > end2:
                break
            elif end1 < s <= end2:
                cnt += 1
                end1 = end2
            end2 = max(end2, e)
        
        return cnt if end2 >= T else -1
            