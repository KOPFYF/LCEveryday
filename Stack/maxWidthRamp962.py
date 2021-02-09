class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # Mono-dec Stack, time O(n), space O(n)  
        stack = [] # to store all candidate start points
        # best candidates idx in dec-order from [9,8,1,0,1,9,4,0,4,1]
        # It's guaranteed to include A[0], as well as the minimum of A.
        for i, a in enumerate(A):
            if not stack or A[stack[-1]] > a:
                stack.append(i)
                #print(stack) # [0,1,2,3] aka [9,8,1,0]
        res = 0
        for j in range(len(A) - 1, -1, -1):
            while stack and A[j] >= A[stack[-1]]:
                res = max(res, j - stack.pop())
        return res
        
        
        # Sliding window, time O(n), space O(n)  
        n = len(A)
        min_arr, max_arr = [A[0]] * n, [A[-1]] * n
        # min_arr[i] is the minimum of all elements till A[i]
        for i in range(1, n):
            min_arr[i] = min(min_arr[i - 1], A[i])
        # max_arr[j] is the maximum of the last len(A) - j elements of A
        for j in range(n - 2, -1, -1):
            max_arr[j] = max(max_arr[j + 1], A[j])
        
        i, res = 0, 0
        for j in range(n):
            if min_arr[i] <= max_arr[j]:
                res = max(res, j - i)
            else:
                i += 1
        return res