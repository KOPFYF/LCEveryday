class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # BFS
        # Use 0/True and 1/False to indicate forward and backward directions, respectively;
        # The bug at most need to reach furthest = max(x, forbideen) + a + b in order to arrive at x, 
        # hence the range of the position of the bug is [0, furthest];
        # Use a Queue to maintain the vectors of the bug, use a Set to avoid forbidden positions and dup
        dq, seen, steps, furthest = deque([(True, 0)]), {(True, 0)}, 0, max(x, max(forbidden)) + a + b
        for pos in forbidden:
            seen.add((True, pos)) 
            seen.add((False, pos)) 
        while dq:
            for _ in range(len(dq)): 
                dir, pos = dq.popleft()
                if pos == x:
                    return steps
                forward, backward = (True, pos + a), (False, pos - b)
                if pos + a <= furthest and forward not in seen:
                    seen.add(forward)
                    dq.append(forward)
                if dir and pos - b > 0 and backward not in seen:
                    seen.add(backward)
                    dq.append(backward)    
            steps += 1         
        return -1