"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # BFS
        if not node:
            return node
        dic = {node: Node(node.val)} # like a seen set
        
        bfs = deque([node])
        while bfs:
            cur = bfs.popleft()
            for nei in cur.neighbors:
                if nei not in dic:
                    bfs.append(nei)
                    dic[nei] = Node(nei.val)
                dic[cur].neighbors.append(dic[nei]) # copy node append copy
        return dic[node]
        
        
        # DFS
        if not node:
            return node
        dic = defaultdict(Node) # like a seen set
        dic[node] = Node(node.val) # init with the first node
        
        def dfs(node, dic):
            for nei in node.neighbors:
                if nei not in dic:
                    dic[nei] = Node(nei.val)
                    dfs(nei, dic)
                dic[node].neighbors.append(dic[nei]) # append all new nodes under
        
        dfs(node, dic)
        return dic[node]
                    