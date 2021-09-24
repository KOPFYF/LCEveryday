class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # bitmask
        m = len(requests)
        
        def check(mask):
            # mask means the request comb we pick, for example
            # m = 5, we pick 3, it could be 11001
            outdegree, indegree = [0] * n, [0] * n
            for i in range(m):
                if mask & (1<<i):
                    u, v = requests[i]
                    outdegree[u] += 1
                    indegree[v] += 1
            return sum(outdegree) if outdegree == indegree else 0
        
        res = 0
        for mask in range(1<<m):
            res = max(res, check(mask))
        return res
            
        
        # combination brute force
        m = len(requests)
        for k in range(m, 0, -1):
            for idxs in itertools.combinations(range(m), k):
                degree = [0] * n # sum of indegree and outdegree
                for i in idxs:
                    u, v = requests[i]
                    degree[u] -= 1
                    degree[v] += 1
                if not any(degree): # net change in employee transfers is zero
                    return k
        
        return 0
                    
                