class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # follow up for max sum subarray, DP idea
        n = len(arr)
        max_ending_here0 = n * [arr[0]]  # no deletion
        max_ending_here1 = n * [arr[0]]  # at most 1 deletion
        for i in range(1, n):
            max_ending_here0[i] = max(max_ending_here0[i - 1] + arr[i], arr[i])
            max_ending_here1[i] = max(max_ending_here1[i - 1] + arr[i], arr[i])
            if i >= 2:
                # try to delete arr[i - 1]
                max_ending_here1[i] = max(max_ending_here1[i], \
                                          max_ending_here0[i - 2] + arr[i])
        return max(max_ending_here1)
    
    
        # space improve to O(1)
        n = len(arr)
        max_ending_here0 = 3 * [arr[0]]  # no deletion
        max_ending_here1 = 3 * [arr[0]]  # at most 1 deletion
        res = arr[0]
        for i in range(1, n):
            max_ending_here0[i % 3] = max(max_ending_here0[(i-1) % 3] + arr[i], arr[i])
            max_ending_here1[i % 3] = max(max_ending_here1[(i-1) % 3] + arr[i], arr[i])
            if i >= 2:
                max_ending_here1[i % 3] = max(max_ending_here1[i % 3], \
                                              max_ending_here0[(i-2) % 3] + arr[i])
            res = max(res, max_ending_here1[i % 3])
        return res