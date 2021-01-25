class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Save all visited sums and corresponding indexes in a priority queue. 
        # Then, once you pop the smallest sum so far, you can quickly identify the next m candidates 
        # for smallest sum by incrementing each row index by 1.
        m, n = len(mat), len(mat[0])
        
        def countArraysHaveSumLessOrEqual(targetSum, r, sum, k):
            # backtrack, count the number of array whose sum is less than or equal to sum
            if sum > targetSum: return 0 # overshoot
            if r == m: return 1
            ans = 0
            for c in range(0, n):
                cnt = countArraysHaveSumLessOrEqual(targetSum, r + 1, sum + mat[r][c], k - ans)
                if cnt == 0: break
                ans += cnt
                if ans > k: break # prune when count > k
            return ans
        
        # binary search the target sum in range [m, 5000*m], 1 <= mat[i][j] <= 5000
        left, right, ans = m, m * 5000, -1
        while left < right:
            mid = left + (right - left) // 2
            cnt = countArraysHaveSumLessOrEqual(mid, 0, 0, k)
            if cnt >= k:
                ans = mid
                right = mid
            else:
                left = mid + 1
        return left
        
    