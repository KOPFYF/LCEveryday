class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree, outdegree = [0] * N, [0] * N
        for u, v in trust:
            # u trusts v, u -> v
            indegree[v - 1] += 1
            outdegree[u - 1] += 1
        
        for i, (ind, outd) in enumerate(zip(indegree, outdegree)):
            if ind == N - 1 and outd == 0:
                return i + 1
        return -1