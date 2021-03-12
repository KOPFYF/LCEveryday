class Fenwick: 
    def __init__(self, n: int): 
        self.nums = [0]*(n+1)
        
    def sum(self, k: int) -> int: 
        ans = 0
        while k: 
            ans += self.nums[k]
            k &= k-1
        return ans 
    
    def add(self, k: int, x: int) -> int: 
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 


class MRUQueue_fw:

    def __init__(self, n: int):
        self.size = n 
        self.tree = Fenwick(n+2000) # buffer for 2000 calls
        self.vals = [0]*(n+2000)
        for i in range(n):
            self.tree.add(i, 1)
            self.vals[i] = i+1

    def fetch(self, k: int) -> int:
        lo, hi = 0, self.size
        while lo < hi: 
            mid = lo + hi >> 1 
            if self.tree.sum(mid) < k: lo = mid + 1
            else: hi = mid 
        self.tree.add(lo-1, -1)
        self.tree.add(self.size, 1)
        self.vals[self.size] = self.vals[lo-1]
        self.size += 1
        return self.vals[lo-1]


class MRUQueue_sqd:
	# square root decomposition
	# O(N) initializaiton & O(sqrt(N)) fetch

    def __init__(self, n: int):
        self.n = n 
        self.nn = int(sqrt(n))
        self.data = []
        self.index = []
        for i in range(1, n+1):
            ii = (i-1)//self.nn 
            if ii == len(self.data): 
                self.data.append([])
                self.index.append(i)
            self.data[-1].append(i)
            
    def fetch(self, k: int) -> int:
        i = bisect_right(self.index, k)-1
        
        x = self.data[i].pop(k - self.index[i])
        for ii in range(i+1, len(self.index)): # shift index
            self.index[ii] -= 1
        if len(self.data[-1]) >= self.nn: # add new bucket 
            self.data.append([])
            self.index.append(self.n)
        self.data[-1].append(x) # append to bucket at end
        if not self.data[i]: # remove empty bucket 
            self.data.pop(i)
            self.index.pop(i)
        return x


class MRUQueue_sl:
	from sortedcontainers import SortedList
	# SortedList (based on binary search tree) from sortedcontainers library

    def __init__(self, n: int):
        self.sl = SortedList((i-1, i) for i in range(1, n+1)) # index, val

    def fetch(self, k: int) -> int:
        # 1. Find the kth item
        _, item = self.sl[k-1]
        # 2. Find the helper element of the last item in the SortedList
        lastItemHelper, _ = self.sl[-1]
		# 3. Remove the kth item
        del self.sl[k-1]
		# 4. Place the removed item last in the SortedList
        self.sl.add((lastItemHelper+1, item))
        # print(self.sl)
        return item


class MRUQueue_bf:
	# brute force, O(N) initialization & fetch

    def __init__(self, n: int):
        self.data = list(range(1, n+1))

    def fetch(self, k: int) -> int:
        self.data.append(self.data.pop(k-1))
        return self.data[-1]