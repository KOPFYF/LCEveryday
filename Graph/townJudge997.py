class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        # Consider trust as a graph, all pairs are directed edge.
        # The point with in-degree - out-degree = N - 1 become the judge.
        trusted = [0] * (N+1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, N+1):
            if trusted[i] == N-1:
                return i
        return -1