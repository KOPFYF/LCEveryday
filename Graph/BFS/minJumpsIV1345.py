class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        for i, v in enumerate(arr):
            d[v].append(i)
            
        n = len(arr)
        bfs = deque([(0, 0)])
        step = 0
        seen_idx, seen_num = set(), set() # pruning
        while bfs:
            cur_node, step = bfs.popleft()
            if cur_node == n - 1:
                return step
            seen_idx.add(cur_node) # track explored positions
            num = arr[cur_node]
            for nxt_node in [cur_node - 1, cur_node + 1] + d[num] * (num not in seen_num):
                if nxt_node not in seen_idx and 0 <= nxt_node < n:
                    bfs.append((nxt_node, step + 1))
            seen_num.add(num) # track explored values