'''
The idea is that we create a sorted version of nums, let say sortedArr.
Then we compare each element belong nums and sortedArr, check if we can swap nums[i] to become sortedArr[i].
If we can't swap nums[i] to become sortedArr[i] then return False
Otherwise, if we can swap all pairs nums[i], sortedArr[i] then return True.
To check if we can swap(nums[i], sortedArr[i]), we need Union-Find to group numbers the same factors together.
Use sieve with time complexity O(N) to calculate spf[x] array, where spf[x] is the smallest prime factor of number x, where x >= 2.
Then iterate each element num in nums:
Get factors of num in O(logNum) since we use spf[x]. Otherwise if we brute force to get factors, time complexity will be O(sqrt(Num)).
Union num and their factors together.
'''
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def sieve(n):
            # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
            # the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
            # smallest prime factor of number x, O(N*log(logN)) ~ O(N)
            spf = [i for i in range(n)]
            for i in range(2, n):
                if spf[i] != i:
                    continue # Skip if it's a not prime number
                for j in range(i * i, n, i):
                    if spf[j] > i:
                        spf[j] = i
            return spf
        
        def getPrimeFactor(num, spf):
            # O(logNum)
            while num > 1:
                yield spf[num]
                num //= spf[num]
        
        spf = sieve(max(nums) + 1)
        dsu = DSU(max(nums) + 1)
        for num in nums:
            for pf in getPrimeFactor(num, spf):
                dsu.union(num, pf)
                
        for x, y in zip(nums, sorted(nums)):
            if dsu.find(x) != dsu.find(y):
                return False
        return True
        
    
    
class DSU:
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if not self.isConnect(x, y):
            self.parents[self.find(x)] = self.find(y)
    
    def isConnect(self, x, y):
        return self.find(x) == self.find(y)
        