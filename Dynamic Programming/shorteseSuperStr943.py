class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        # each word is a node, the edge is the common len bbetween nodes
        # G[2][1] means node 1 after node 2 would save 3
        # => find longest path to go through all nodes
        def build_edge(s1, s2):
            # say s1, s2 = "c(atg)", "(atg)a", we will return 3
            for i in range(1, len(s1)):
                s1_right = s1[i:]
                if s2.startswith(s1_right):
                    # s1_right = s2_left
                    return len(s1) - i
            return 0
        
        n = len(A)
        G = [[0] * n for _ in range(n)] # adjcent matrix of graph
        for i in range(n):
            for j in range(i + 1, n):
                G[i][j] = build_edge(A[i], A[j])
                G[j][i] = build_edge(A[j], A[i])
        
        # 2^n states
        dp = [[0] * n for _ in range(1 << n)]
        # deque for BFS, (node, mask, path, s_len)
        dq = deque([(i, 1 << i, [i], 0) for i in range(n)])
        l = -1 # record the maximum s_len
        P = [] # record the path corresponding to maximum s_len
        while dq:
            node, mask, path, dis = dq.popleft()
            if dp[mask][node] > dis:
                continue
            if mask == (1 << n) - 1 and dis > l:
                # to the end and find better solution, update
                P, l = path, dis 
                continue
            for i in range(n):
                # loop each candidate
                nxt_mask = mask | (1 << i)
                # case1: make sure that each node is only traversed once
                # case2: only if we can get larger save length, we consider it.
                if nxt_mask != mask and dp[mask][node] + G[node][i] >= dp[nxt_mask][i]:
                    dp[nxt_mask][i] = dp[mask][node] + G[node][i]
                    dq.append((i, nxt_mask, path + [i], dp[nxt_mask][i]))
        
        res = A[P[0]]
        for i in range(1, len(P)):
            cur, prev = P[i], P[i - 1] # cur id, and prev id
            edge = G[prev][cur] # get the overlapping len
            res += A[cur][edge:] # substring of right part 
        return res 



class Solution2:
    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        # Building the graph
        graph = [[0] * n for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i == j: continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    if word1[-k:] == word2[:k]:
                        graph[i][j] = k
                        break
        
        # Recursion. i is a mask to represent the ordering. k is the last node in the ordering.
        memo = {}
        def search(i, k):
            if (i, k) in memo: return memo[i, k]
            if not (i & (1 << k)): return ''
            if i == (1 << k): return A[k]
            memo[i, k] = ''
            for j in range(n):
                if j != k and i & (1 << j):
                    candidate = search(i ^ (1 << k), j) + A[k][graph[j][k]:]
                    if memo[i, k] == '' or len(candidate) < len(memo[i, k]):
                        memo[i, k] = candidate
            return memo[i, k]
        
        # Finding the best
        res = ''
        for k in range(n):
            candidate = search((1 << n) - 1, k)
            if res == '' or len(candidate) < len(res):
                res = candidate
        return res 