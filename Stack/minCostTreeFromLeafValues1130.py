class Solution1:
    def mctFromLeafValues(self, arr: List[int]) -> int:
    	# greedy, O(n^2), put big leaf nodes close to the root to limit its contribution to total sum
        res = 0
        while (n:=len(arr)) > 1:
            idx = arr.index(min(arr))
            if 0 < idx < n - 1: 
                # min node in the middle, candy crush with the smaller neighbor
                res += arr[idx] * (min(arr[idx - 1], arr[idx + 1]))
            else:
                # min node at 2 ends, if idx = 0, left end and only right neighbor is valid
                res += arr[idx] * (arr[idx + 1] if idx == 0 else arr[idx - 1])
            arr.pop(idx) # pop takes O(n)
        return res

        # shorter version, but not quite readable from lee215
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res


class Solution2:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # DP, time O(n^3), space O(n^2)
        # dp(i, j) is the answer for the subarray arr[i]..arr[j]
        # For each possible way to partition the subarray i <= k < j
        # the answer is max(arr[i]..arr[k]) * max(arr[k+1]..arr[j]) + dp(i, k) + dp(k+1, j).
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= j:
                return 0
            res = float('inf')
            for k in range(i, j):
                # k is the pivot
                res = min(res, max(arr[i:k + 1]) * max(arr[k + 1:j + 1]) + dfs(i, k) + dfs(k + 1, j))
            memo[(i, j)] = res
            return res
        
        return dfs(0, len(arr) - 1)


class Solution3:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # monotonic stack, time O(n), 单调递减栈
        # find the next greater element in the array, on the left and one right.
        stack = [float('inf')]
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                cur = stack.pop()
                if stack:
                    res += cur * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
