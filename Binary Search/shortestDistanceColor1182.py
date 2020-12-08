class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = defaultdict(list)
        for i, c in enumerate(colors):
            maps[c].append(i)
        
        res = []
        for qi, qc in queries:
            if qc in maps:
                idx = bisect.bisect_left(maps[qc], qi) 
                if idx == 0:
                    res.append(maps[qc][0] - qi)
                elif idx == len(maps[qc]):
                    res.append(qi - maps[qc][-1])
                else:
                    # take the min of the left and right
                    res.append(min(maps[qc][idx] - qi, \
                                   qi -  maps[qc][idx - 1]))
            else:
                res.append(-1)
        return res