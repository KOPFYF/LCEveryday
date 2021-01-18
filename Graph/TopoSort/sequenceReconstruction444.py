class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        nodes = set([v for seq in seqs for v in seq])
        graph = defaultdict(list)
        indegrees = {v: 0 for v in nodes}
        
        # build graph
        for seq in seqs:
            for i in range(len(seq) - 1):
                x, y = seq[i], seq[i + 1]
                graph[x].append(y)
                indegrees[y] += 1

        # bfs
        res = []
        bfs = deque([k for k, v in indegrees.items() if v == 0])
        while bfs:
            if len(bfs) != 1: return False # path not unique
            cur = bfs.popleft()
            res.append(cur)
            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    bfs.append(nxt)
        
        # print(indegrees)
        return sum(indegrees.values()) == 0 and res == org
        # return len(res) == len(nodes) and res == org