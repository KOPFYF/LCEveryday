class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        # top-down DP, time out for the last 20 testcases 
        # because this is a general template that could solve all (x, y, z) combinations
        n = len(A)
        print(sum(A))
        memo = {}
        def dfs(x, y, idx):
            if idx >= n:
                return 0
            if (x, y, idx) in memo:
                return memo[(x, y, idx)]
            tmp0 = dfs(x, y, idx + 1) # dont take A[idx]
            res, tmp1, tmp2 = -1, -1, -1
            if x > 0 and idx + L - 1 < n:
                tmp1 = dfs(x - 1, y, idx + L) + sum(A[idx:idx + L])
            if y > 0 and idx + M - 1 < n:
                tmp2 = dfs(x, y - 1, idx + M) + sum(A[idx:idx + M])
            res = max(tmp0, tmp1, tmp2)
            memo[(x, y, idx)] = res
            print(memo)
            return res
        
        return dfs(1, 1, 0)


def maxSumThreeNoOverlap(A, x, y, z):
	n = len(A)
	memo = {}
	# top-down DP with memory
	def dfs(x, y, z, idx):
		# print('**** n', n, A)
		if idx >= n:
			return 0
		if (x, y, z, idx) in memo:
			return memo[(x, y, z, idx)]
		tmp0 = dfs(x, y, z, idx + 1) # dont take A[idx], move on to next index
		# res, tmp1, tmp2, tmp3 = 0, 0, 0, 0 # nums can be negative, should init with -inf
		res, tmp1, tmp2, tmp3 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
		if x > 0 and idx < n: # include A[idx] with len=1 window
			tmp1 = dfs(x - 1, y, z, idx + 1) + A[idx]
		if y > 0 and idx + 1 < n: # include A[idx: idx + 2] with len=2 window
			tmp2 = dfs(x, y - 1, z, idx + 2) + A[idx] + A[idx + 1]
		if z > 0 and idx + 2 < n: # include A[idx: idx + 3] with len=3 window
			tmp3 = dfs(x, y, z - 1, idx + 3) + A[idx] + A[idx + 1] + A[idx + 2]
		res = max(tmp0, tmp1, tmp2, tmp3)
		if res != float('-inf'):
			memo[(x, y, z, idx)] = res
			return res

	
	ans = dfs(x, y, z, 0)
	print(memo)
	return ans

A = [1,2,3,4,76,6,7,0,99,1,2,95]
x, y, z = 1, 2, 2
print('sum A: ', sum(A))

ans = maxSumThreeNoOverlap(A, x, y, z)
print('dp answer:', ans)