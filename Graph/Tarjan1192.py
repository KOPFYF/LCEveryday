'''
      u
	/  \\     , Assume we start DFS from 'u' whose depth is 0, and at the first step we walk from 'u' to 'v', we will update depth of 'v' to 1. Then, we walk from 'v' to 'm', and update depth of 'm' to 2. 
   m  - v      Finally, we walk from 'm' to 'u' and see it has been reached with depth equals to 0 (which I called 'minimum depth earlier'), we backtrack the depth of 'm' to 0, and thus backtrack the depth of 'v' to 0.
	           Because all the nodes have the minimum reachable depths equal to 0, no depth is strictly larger than others, therefore, all the 3 connections are not critical edge. 
               
     u
	/  \\     , Following from the previous example we know that if we start DFS from node 'u', in the end nodes 'u', 'v', 'm' would have a minimum reachable depths equal to 0.
   m  - v      But, 'n' will have a depth of '2'. why it is not updated through backtracking? Because the depth of n is originall propagated through m, and when DFS reached 'n' the search of that branck is stopped.
  /            When the depth 0 is backtracking from 'u' to 'm' and to 'v', this backtracking would not go through m->n again! (This is the forward propagate of the original DFS!), so the depth of n remains 2.
 n          Finally we see that (m,n) is a critical connection.
'''

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # Tarjan's algorithm
        low = [0] * n # the lowest order of vertex that can reach this vertex i
        edges = defaultdict(list)
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
            
        def dfs(rank, cur, prev):
            low[cur], res = rank, []
            for nxt in edges[cur]:
                if nxt == prev: 
                    continue # dont go back
                if not low[nxt]: 
                    res += dfs(rank + 1, nxt, cur)
                # take the min of the current vertex's and next vertex's ranking
                low[cur] = min(low[cur], low[nxt])
                # if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection
                if low[nxt] > rank:
                    res.append([cur, nxt])
            return res
        
        return dfs(1, 0, -1)