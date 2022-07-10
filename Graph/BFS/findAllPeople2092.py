class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # build a graph for all the meetings happening at the same time and then BFS or DFS the nodes
        know = {0, firstPerson} # people know secret, like a global seen set
        
        s = sorted(meetings, key=lambda x:x[2])  # sort by meeting time
        for time, group in groupby(s, key=lambda x:x[2]):  # group by meeting time
            q = set() # queue
            graph = defaultdict(set)
            for x, y, _ in group:
                graph[x].add(y)
                graph[y].add(x)
                if x in know: q.add(x)
                if y in know: q.add(y)
            
            # go through q
            q = deque(q)
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if nxt not in know:
                        know.add(nxt)  # add new people with secret
                        q.append(nxt)
        return know
    
    
    
        know = {0, firstPerson}
        # events = sorted(meetings, key=lambda x:x[-1])
        graph = defaultdict(dict)
        for p1, p2, t in meetings:
            if p1 not in graph[t]:
                graph[t][p1] = [p2]
            else:
                graph[t][p1].append(p2)
            if p2 not in graph[t]:
                graph[t][p2] = [p1]
            else:
                graph[t][p2].append(p1)
        
        print(graph)
        for t in sorted(graph.keys()):
            # bfs on each timestamp
            seen = set()
            for p in graph[t]:
                if p in know and p not in seen:
                    bfs = deque([p])
                    seen.add(p)
                    while bfs:
                        cur = bfs.popleft()
                        for nxt in graph[t][cur]:
                            if nxt not in seen:
                                bfs.append(nxt)
                                seen.add(nxt)
                                know.add(nxt)
        return list(know)
                    
            
        
        