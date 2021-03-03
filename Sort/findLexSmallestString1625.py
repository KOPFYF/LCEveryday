class Solution_BFS:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # print(self._add("3456", 5))
        # print(self._rotate("3456", 1))
        # BFS
        seen = set()
        bfs = deque([s])
        while bfs:
            cur = bfs.popleft()
            if cur not in seen:
                seen.add(cur)
                bfs += [self._add(cur, a)] + [self._rotate(cur, b)]
        return min(seen)
        
    def _add(self, s, a):
        new = ""
        for i in range(len(s)):
            if i % 2 != 0:
                new += str(int(s[i])+a)[-1]
            else:
                new += s[i]
        return new
    
    def _rotate(self, s, b):
        n = len(s)
        return s[n-b:] + s[:n-b]



class Solution_DFS:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # dfs
        def dfs(s: str) -> None:
            if s not in seen:
                seen.add(s)
                self.smallest = min(s, self.smallest)
                addA = list(s)
                for i, c in enumerate(addA):
                    if i % 2 == 1:
                        addA[i] = str((int(c) + a) % 10)
                dfs(''.join(addA))
                dfs(s[b :] + s[: b])
                
        self.smallest = s
        seen = set()
        dfs(s)
        return self.smallest
        