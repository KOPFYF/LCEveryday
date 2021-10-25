class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = collections.Counter(s)
        res = []
        
        for ch in order: # linear scan order
            res.append(ch * cnt[ch])
            cnt[ch] = 0 # marked as visited
        
        for ch in cnt: # leftover
            res.append(ch * cnt[ch])
        
        return "".join(res)