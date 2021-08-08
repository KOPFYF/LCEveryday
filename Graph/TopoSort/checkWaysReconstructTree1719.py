'''
Summary
The thing to note is that if something is the root of a subtree, then it must be paired with all of its descendants (and its ancestors). So a parent's pairings will always contain a child's pairings.

So, if we use the pairs to create an adjacency list, we can proceed greedily by always selecting the node with greatest degree (here, we're talking about the degree in the graph formed by pairs, not the tree), and finding its parent. Since we proceed top-down, the already visited adjacencies are the node's ancestors, and its parent is the one with least degree. We then have to check the condition that the parent's adjacencies contain the child's adjacencies (aside from itself).

So:

1. Construct adjacency list from pairs
2. Repeatedly take node with greatest degree
3. Choose parent to be adjacency with least degree among those that have been visited
    a. If the node is the first, i.e. parent is none, check if node is the root, else return 0.
4. Parent's adjacencies must contain the node's adjacencies, except the parent itself, else return 0.
5. If parent and it have the same degree, you could visit them in either order, so there might be multiple answers.
6. If you iterated through every node, return 2 or 1 depending on step 6.

'''
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u, v in pairs:
            graph[u].add(v)
            graph[v].add(u)
        
        print(graph)
        
        n = len(graph)
        res = False
        ancestor = set()
        for u in sorted(graph.keys(), key=lambda x:len(graph[x]), reverse=True): # process nodes with greatest degree 
            print(u, ancestor)
            # selecting the node with least degree as parent
            parent = min((graph[u] & ancestor), key=lambda x:len(graph[x]), default=0)
            ancestor.add(u)
            if parent:
                # since u's ancestors are p + p's ancestors and u + u's descendants are all p's descendants
                if not graph[u].issubset(graph[parent] | {parent}):
                    return 0
                # parent and it have the same degree, you could visit them in either orde
                res |= (len(graph[u]) == len(graph[parent]))
            elif len(graph[u]) != n - 1: # check if u is root
                return 0
        return 1 + res



class Solution1:
    # https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/discuss/1009238/Python-dfs-solution-explained
    def checkWays(self, pairs: List[List[int]]) -> int:
        def find_trees(nodes): 
        # In order to be a root of a tree, the root must be connected 
        # to all other nodes, so number of connections from a possible 
        # root should be len(nodes) - 1
        rank_needed = len(nodes) - 1
        
        pos_roots = []
        for node in nodes: 
            if len(g[node]) == rank_needed: 
                pos_roots.append(node)
        
        # If there are not possible roots, we return 0
        if len(pos_roots) == 0: return 0
                
        # Pick the first first possible root to try
        root = pos_roots[0]
        
        # Now we need to build out the rest of our tree. There will be a 
        # branch for each "group" of connections. If all the nodes are 
        # connected, there will be one long branch. If none of the nodes 
        # are connected, there will be len(branches) groups. So for each group
        # of connected nodes, we will run find_trees(group). If any of 
        # the runs fail, then ancestors cannot be valid roots either. 
        # If any runs produce 2 or more valid trees with no other groups failing, 
        # failing, we know we have 2 or more valid trees total. 
        
        # Remove the root from the rest of the nodes connections because
        # the root should not appear again in the tree.
        for node in nodes: 
            if node != root: 
                g[node].remove(root)
        
        # Create groups of connected nodes
        groups = defaultdict(set)
        seen = set()
        def dp(node, i): 
            seen.add(node)
            groups[i].add(node)
            for nei in g[node]: 
                if nei not in seen: 
                    dp(nei, i)
        i = 0
        for node in nodes: 
            if node != root and node not in seen: 
                dp(node, i)
                i += 1
        
        # Number of valid sub trees for each group
        cand = [find_trees(group) for group in groups.values()]
        
        # If there is a 0 in cand, then a group failed to make 
        # a valid subtree so we can't make any valid subtrees. 
        if 0 in cand: return 0
        
        # Given no 0's, if there is a 2 in cand, then we have 
        # at least 2 valid trees total. 
        if 2 in cand: return 2
        
        # If we got to this point without returning, we have
        # all 1's in cand. If there were 
        # 2 possible roots to begin with, we could switch positions of the
        # possible roots to get 2 valid trees. 
        if len(pos_roots) > 1: return 2
        
        # If we still haven't returned, then there must be only 
        # one possible root, with one valid tree, so we return 1. 
        return 1
        
    return find_trees(set(g.keys()))
                
            