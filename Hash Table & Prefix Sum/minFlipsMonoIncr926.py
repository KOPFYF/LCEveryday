class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        final pattern: 0001111, find the cutoff i
                          i 
        cnt0 counts 0 after index i, cnt1 counts 1 before index i
        res would be cnt0 + cnt1
        '''
        # presum, O(n)/O(1)
        n = len(s)
        cnt0, cnt1 = s.count('0'), 0 
        res = n - cnt0
        
        for ch in s:
            if ch == '0':
                cnt0 -= 1
            else:
                res = min(res, cnt1 + cnt0)
                cnt1 += 1
        return res
            
