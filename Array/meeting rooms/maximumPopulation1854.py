class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # sweep line + sort, O(nlogn)
        dates = []
        for s, e in logs:
            dates.append((s, 1))
            dates.append((e, -1))
        
        dates.sort() # sort by time
        
        res, max_ppl, ppl = 0, 0, 0
        for yr, diff in dates:
            ppl += diff
            if ppl > max_ppl:
                max_ppl = ppl
                res = yr
        return res
        
        
        # sweep line, O(n)
        arr = [0] * 2051
        res = 0
        
        for s, e in logs:
            arr[s] += 1
            arr[e] -= 1
            
        for yr in range(1950, 2050):
            arr[yr] += arr[yr - 1]
            if arr[yr] > arr[res]:
                res = yr
        return res