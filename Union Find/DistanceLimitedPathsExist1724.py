class DistanceLimitedPathsExist:
    '''
    Sort the edgeList with weight and connect the nodes in the order of weight.
    For each weight value, store the current status of connection
    Use binary search to find the index of each query, and then check the current status
    '''
    def __init__(self, n, edgeList):
        parent = list(range(n))

        self.parents = [parent.copy()]
        self.weights = [0]

        edgeList.sort(key=lambda x: x[2])
        for index, (i, j, weight) in enumerate(edgeList):  # for cur weight, connect i,j
            self._union(parent, i, j)
            if index == len(edgeList) - 1 or weight != edgeList[index + 1][2]:
                # Save a new version
                self.weights.append(weight)  # save the weight keys, this is the max weight in that MST
                self.parents.append(parent.copy())  # save the connection for cur weight
                # print('www', self.weights)
                # print('ppp', self.parents)

    def _union(self, parent: List[int], x: int, y: int):
        parent[self._find(parent, y)] = self._find(parent, x)

    def _find(self, parent: List[int], node: int):
        if parent[node] != node:
            parent[node] = self._find(parent, parent[node])
        return parent[node]

    def query(self, p, q, limit):
        index = bisect.bisect_left(self.weights, limit) - 1
        parent = self.parents[index]
        return self._find(parent, p) == self._find(parent, q)
    
# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)