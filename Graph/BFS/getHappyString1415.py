class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # level BFS
        bfs = ['a', 'b', 'c']
        level = 1
        d = {'a': ('b', 'c'), 'b': ('a', 'c'), 'c': ('a', 'b')}
        
        while bfs:
            if level == n:
                if k <= len(bfs):
                    return bfs[k - 1]
                else:
                    return ""
            nxt_bfs = []
            for s in bfs:
                for nxt_ch in d[s[-1]]:
                    nxt_s = s + nxt_ch
                    nxt_bfs.append(nxt_s)
            
            level += 1
            bfs = nxt_bfs