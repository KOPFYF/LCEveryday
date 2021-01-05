class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # LIS O(nlogn), target contains no duplicates!!
        # If a value is not existed in target, we just skip it. 
        # Now the LCS between target and arr is the same as the LIS of the index array A.
        dic = {num: i for i, num in enumerate(target)}
        A = []
        for num in arr:
            if num in dic:
                A.append(dic[num])
        # target: [6,4,8,1,3,2]
        # arr: [4,7,6,2,3,8,6,1]
        print(dic) # {6: 0, 4: 1, 8: 2, 1: 3, 3: 4, 2: 5} 
        print(A) # [1, 0, 5, 4, 2, 0, 3]
        return len(target) - self.lengthOfLIS(A)
    
    def lengthOfLIS(self, nums):
        if not nums: 
            return 0
        piles = [] 
        for num in nums:
            index = bisect.bisect_left(piles, num)
            if index == len(piles):
                piles.append(num)
            else:
                piles[index] = num
            print('LIS:', piles)
            # LIS: [1]
            # LIS: [0]
            # LIS: [0, 5]
            # LIS: [0, 4]
            # LIS: [0, 2]
            # LIS: [0, 2]
            # LIS: [0, 2, 3]
        return len(piles)
    
    
        # LIS O(nlogn)
        ha = {a: i for i, a in enumerate(target)}
        stack = []
        for a in arr:
            if a not in ha: 
                continue
            i = bisect.bisect_left(stack, h[a])
            if i == len(stack):
                stack.append(0)
            stack[i] = h[a]
        return len(target) - len(stack)
    
 
                
        # DP TLE    
        m, n = len(target), len(arr)
        @lru_cache(None)
        def dfs(i, j):
            if i == m: # target to the end, no more op needed
                return 0
            if j == n: # arr to the end, 
                return m - i
            
            if target[i] == arr[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(dfs(i + 1, j) + 1, dfs(i, j + 1)) 
        
        return dfs(0, 0)
            
            
            