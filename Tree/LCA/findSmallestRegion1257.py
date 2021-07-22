class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        # Space O(n) not optimal
        parents = {region[i]:region[0] for region in regions for i in range(1, len(region))}
        ancestry_history = {region1}
        while region1 in parents:
            region1 = parents[region1]
            ancestry_history.add(region1)
        while region2 not in ancestry_history:
            region2 = parents[region2]
        return region2
        
        # Soln 2, TLE
        for region in regions:
            for i in range(1, len(region)):
                parent = Node(region[0])
                node = Node(region[i])
                node.parent = parent
                if region[i] == region1:
                    node1 = node
                if region[i] == region2:
                    node2 = node
        
        p1, p2 = node1, node2
        while p1 != p2:
            # when p1 points to root (i.e p1.parent is None), assign q to p1
            p1 = p1.parent if p1.parent else node2
            p2 = p2.parent if p2.parent else node1
            
        return p1.val
        
                    
        
        
        