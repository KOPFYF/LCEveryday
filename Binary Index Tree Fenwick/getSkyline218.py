    def getSkyline(self, buildings):
        def update(p, h):
            while p > 0: # scope of h is towards left
                bit[p] = max(bit[p], h)
                p -= p & -p
        def query(p):
            ret = 0
            while p <= len(bit): # check anything to the right that has a higher value
                ret = max(ret, bit[p])
                p += p & -p
            return ret
        
        ret, ends, points = [], {}, []
        for i, b in enumerate(buildings):
            points += ((b[0], -1, -b[2]), (b[1], 1, -b[2]))
            ends[points[-2]] = points[-1]
        
        bit = [0] * (len(points) + 1)
        points.sort()
        idx = {points[i]: i for i in range(len(points))} # keep sorted index
        
        for i, p in enumerate(points):
            if p[1] == -1:
                end = ends[p]
                update(idx[end], -p[-1]) # end idx is exclusive
            h = query(i+1) # start idx is inclusive
            if not ret or ret[-1][1] != h:
                if ret and ret[-1][0] == p[0]:
                    ret[-1][1] = h
                else:
                    ret.append([p[0], h])
        return ret