class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Suppose you have 3 MHT with root r1, r2, r3 respectively. it could be shown as
        # subtree1 ~ r1 ~ (some nodes in between) ~ r2 ~ (some nodes in between) ~ r3 ~ subtree2.
        # You could see, in this case, r2.height < r1.height and r2.height < r3.height.
        # Thus, it is impossible to have more than 2 MHT roots.

        if n == 1: 
            return [0]
        G = defaultdict(set)       
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
            
        # multi-end BFS, start from leaves
        dq = deque([v for v in range(n) if len(G[v]) == 1])
        # print(dq)
        while n > 2:
            # remove all leaves
            n -= len(dq)
            for _ in range(len(dq)):
                l = dq.popleft() # this leaf only has one neighbor
                v = G[l].pop() # get that neighbor
                G[v].remove(l) # remove leave from that neighbor
                if len(G[v]) == 1:
                    # new leaf
                    dq.append(v)
        return list(dq)


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        s = set(range(n))
        while len(s) > 2:
            # find all leaves and shrink
            leaves = set(v for v in s if len(G[v]) == 1)
            # remove leaves from s & G
            s -= leaves
            for l in leaves:
                for v in G[l]:
                    G[v].remove(l)
        
        return list(s)