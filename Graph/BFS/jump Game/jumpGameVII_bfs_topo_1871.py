class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # BFS O(n)/O(n)
        bfs = deque([0])
        seen = set([0])
        mx = 0
        while bfs:
            i = bfs.popleft()
            if i == len(s) - 1:
                return True
            for j in range(max(mx + 1, i + minJump), min(i + maxJump + 1, len(s))):
                if s[j] == '0' and j not in seen:
                    seen.add(j)
                    bfs.append(j)
            # mx = max(mx, i + maxJump) # all before i + maxJump
            mx = i + maxJump
        return False
    
        # TLE, with no mx trick
        bfs = deque([0])
        seen = set([0])
        mx = 0
        while bfs:
            i = bfs.popleft()
            if i == len(s) - 1:
                return True
            for j in range(i + minJump, min(i + maxJump + 1, len(s))):
                if s[j] == '0' and j not in seen:
                    seen.add(j)
                    bfs.append(j)
        return False