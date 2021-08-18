class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        '''
		Because we actually need to return the path, dp[i][j] is a tuple
		where the first element is minimum edit distance w/ path ending at node i and targetPath ending at j
		and the second element is the actual path.
        '''
        # O(m^2n) / O(m^2n)
        m = len(targetPath)
        graph = defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)
        
        dp = [[(float('inf'), [-1] * (j+1)) for j in range(m)] for _ in range(n)]
        # print(dp) # dp[i][j] is a tuple (mindist, [path])
        for j in range(m): # paths
            for i in range(n): # nodes
                if j == 0:
                    dp[i][j] = (int(names[i] != targetPath[j]), [i])
                else:
                    dist, path = min(dp[ii][j-1] for ii in graph[i])
                    dp[i][j] = (dist + (names[i] != targetPath[j]), path + [i])
        return min(dp[i][-1] for i in range(n))[1]