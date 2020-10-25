class Solution0(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 1d dp, 36 ms beats 100%, fastest!!! 
        # dp[k] key is k elements, value is a set of possible sums
        n, s = len(A), sum(A)
        if not any(s*k%n == s*(n-k)%n == 0 for k in range(1, n // 2 + 1)): 
            # we need at least one possible k
            return False 

        dp = collections.defaultdict(set)
        dp[0].add(0)
        for i in A:
            for k in range(n // 2, 0, -1):
                for j in dp[k - 1]: # backtrack from the last case, k - 1 elements 
                    dp[k].add(i + j) 
                    if (i + j) * n == s * k : 
                        # if (current value + last sum) == target sum s * k / n
                        return True 
        return False


class Solution1(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # DFS, 116 ms
        # Math tip: if s1/n1 == s2/n2 then s1/n1 = s2/n2 = (s1+s2)/(n1+n2) = sum(A)/len(A) = avg(A)
        # check if total k elements with sum = k * avg(A), turn to N-sum problem
        
        n, s, memo = len(A), sum(A), {}
        
        def dfs(target, k, pos):
            # find a subset of k elements from A with sum = target
            if k < 0 or k > n - pos: # index overflow
                return False
            if k == 0 or pos == n: # loop to the end, check target == 0
                return target == 0 
            if (target, k, pos) in memo: 
                return memo[(target, k, pos)]
            
            # dfs either takes the i-th or not
            memo[(target, k, pos)] = dfs(target - A[pos], k - 1, pos + 1) or \
                                     dfs(target, k, pos + 1) # dont take i-th
                                     
            return memo[(target, k, pos)]
    
        for j in range(1, n // 2 + 1):
            if s * j % n == 0 and dfs(s * j // n, j, 0):
                return True
        return False


class Solution2(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # dp, O(n^3*sum) 2856 ms
        n, s = len(A), sum(A)
        
        def dp(nums, n, target):
            # dp[i][j] means j elements sum up to i is true or not
            dp = [[False] * (n + 1) for _ in range(target + 1)]
            dp[0][0] = True
            for num in nums:
                for i in range(target, num - 1, -1): # reverse top down
                    for j in range(n, -1, -1):
                        if (dp[i - num][j - 1]):
                            dp[i][j] = True;
            return dp[target][n]
        
        for j in range(1, n // 2 + 1):
            if s * j % n == 0 and dp(A, j, s * j // n):
                return True
        return False
        

class Solution3(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 1d dp 552 ms, only check target, using set to save memo
        A.sort(reverse=True)
        dp = {0: 0} # base case, sum to zero
        n, s = len(A), sum(A)
        for a in A:
            for k in sorted(dp.keys(), reverse=True): # reverse top down
                dp[k + a] = dp[k] + 1
                k += a
                v = dp[k]
                if v and n - v and k * (n - v) == (s - k) * v:
                    return True
        return False      
    