"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # soln 0, bottom up, 2 pointers
        p1, p2 = p, q
        while p1 != p2:
            # print(p1.val, p2.val)
            # when p1 points to root (i.e p1.parent is None), assign q to p1
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1
    
        # soln 1
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent
        
        while p:
            if p.val in visited: return p
            visited.add(p.val)
            p = p.parent
        return None
    
        