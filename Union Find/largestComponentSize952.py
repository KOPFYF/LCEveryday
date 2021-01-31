class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution1:
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: 
            	primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])

        return max(Counter([UF.find(i) for i in range(n)]).values())


class Solution2:
    def largestComponentSize(self, A: List[int]) -> int:
        factor_to_num_index = collections.defaultdict(int)
        uf = UF(len(A))
        for ind, num in enumerate(A):
            for factor in range(2, int(math.sqrt(num) + 1)):
                if num % factor == 0:
                    for fac in (factor, num // factor):
                        if fac in factor_to_num_index:
                            # one index already claimed, so union that one with current
                            uf.union(ind, factor_to_num_index[fac])
                        else:
                            # no index has claimed the factor yet
                            factor_to_num_index[fac] = ind
            # union the same num
            if num not in factor_to_num_index:
                factor_to_num_index[num] = ind
            else:
                uf.union(ind, factor_to_num_index[num])
        return max(uf.size)
    
    
class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            size_x, size_y = self.size[px], self.size[py]
            if size_x < size_y:
                self.parent[px] = py
                self.size[py] += size_x
            else:
                self.parent[py] = px
                self.size[px] += size_y
        