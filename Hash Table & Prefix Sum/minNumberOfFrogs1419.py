class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = collections.Counter(croakOfFrogs) 
        for k in 'roak':
            if cnt[k] != cnt['c']:
                return -1
        
        d = defaultdict(int)
        res = 0
        for ch in croakOfFrogs:
            if d['c'] >= d['r'] >= d['o'] >= d['a'] >= d['k']:
                d[ch] += 1
                res = max(res, d['c'] - d['k']) # for example, c=2,k=0, need at least 2 frogs
            else:
                # c should have the most counts, since it's a seq
                return -1
        # print(d)
        return res