class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # soln1
        d = collections.defaultdict(int)
        for i, j, c in segments:
            d[i] += c
            d[j] -= c
        # print(d)
        res = []
        prev = 0
        for j in sorted(d):
            if d[prev]:
                res.append([prev, j, d[prev]])
            d[j] += d[prev]
            prev = j
        return res
    
        # soln 2
        vals = []
        for start, end, color in segments: 
            vals.append((start, +color))
            vals.append((end, -color))
        
        res = []
        prefix = prev = 0 
        for x, c in sorted(vals): 
            if prev < x and prefix: 
                res.append([prev, x, prefix])
            prev = x
            prefix += c 
        return res 
    
        # my soln
        intervals = []
        for (s, e, w) in segments:
            intervals.append((s, w))
            intervals.append((e, -w))
        intervals.sort()
        
        intervals2 = []
        cur = 0
        for cut, diff in intervals:
            cur += diff
            intervals2.append([cut, cur])
        
        intervals3 = [intervals2[0]]
        for cut, cur in intervals2[1:]:
            if cut == intervals3[-1][0]:
                intervals3[-1][1] = cur
            else:
                intervals3.append([cut, cur])

        res = []
        for (a1, b1), (a2, b2) in zip(intervals3, intervals3[1:]):
            if b1:
                res.append([a1, a2, b1])
        return res
            
                
            
            
                
            