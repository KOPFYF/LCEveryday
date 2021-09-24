class Solution:
    def minimumDeletions(self, s: str) -> int:
        # find for every index the number of Bs before it and the number of A's after it
        # suffix & prefix
        cnt, n = Counter(s), len(s)
        # print(cnt) # Counter({'b': 75, 'a': 60})
        cnt_a, cnt_b, res = cnt['a'], 0, min(cnt['a'], cnt['b'])
        for i, ch in enumerate(s):
            if ch == 'a':
                cnt_a -= 1  
            else:
                # res = min(res, cnt_a + cnt_b)
                cnt_b += 1
            res = min(res, cnt_a + cnt_b) # wrong on the last 2 cases, should be 60 but return 61
        return res
                
            
            
            