class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # backtracking, like permutation II, O(n!)
        nums.sort()
        @lru_cache(None)
        def check(num):
            return pow(int(sqrt(num)), 2) == num
        
        res = 0
        def dfs(nums, path): # perm II
            nonlocal res
            if not nums:
                res += 1
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                if path and not check(path[-1] + nums[i]):
                    continue
                dfs(nums[:i] + nums[i+1:], path + [nums[i]])
                
        dfs(nums, [])
        # print(res)
        return res


class Solution_bt:
    def numSquarefulPerms(self, A: List[int]) -> int:        
        # backtracking, like permutation II, O(n!)
        res = []
        self.dfs(sorted(A), [], res)
        return len(res)
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # skip duplicates
            if path and not self.square(path[-1]+nums[i]):
                continue # backtracking without going further 
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
    def square(self, num):
        from math import sqrt
        return pow(int(sqrt(num)), 2) == num


class Solution_dp_bitmask:
    def numSquarefulPerms(self, A: List[int]) -> int:
        # dp bitmask, dfs + memo, O(n^2 2^n)
        n = N = len(A)
        def edge(x, y):
            r = math.sqrt(x + y)
            return int(r + 0.5) ** 2 == x + y

        graph = defaultdict(list)
        for i in range(n):
            for j in range(i):
                if edge(A[i], A[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        # find num of hamiltonian paths in graph
        @lru_cache(None)
        def dfs(node, mask):
            if mask == (1 << n) - 1: # reach full
                return 1
            
            res = 0
            for nxt in graph[node]:
                if (mask >> nxt) & 1 == 0: # if nxt bit not in mask
                    res += dfs(nxt, mask | (1 << nxt)) # put it in and try
            return res

        res = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            res //= math.factorial(v)
        return res
        
        
