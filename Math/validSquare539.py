class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        def dist(p, q):
            return (p[0] - q[0])**2 + (p[1] - q[1])**2
        
        dists = [] # 6 edges in total
        ps = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i+1, 4):
                p, q = ps[i], ps[j]
                dists.append(dist(p, q))
        dists.sort()
        
        if dists[0] == dists[1] == dists[2] == dists[3]:
            if dists[4] == dists[5] == 2 * dists[0]:
                return True
        return False
        

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        
        dists = collections.Counter()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dists[self.getDistance(points[i], points[j])] += 1
        
        # the length of diagonal
        # the length of the edge
        # diag = sqrt(2) * edge
        print(dists) # value has to be 4, 2 (4 edges and 2 diags)
        
        return len(dists.values()) == 2 and 4 in dists.values() and 2 in dists.values()
    
    def getDistance(self, p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2