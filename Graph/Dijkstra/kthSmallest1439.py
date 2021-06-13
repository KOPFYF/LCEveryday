class Solution(object):
    def kthSmallest(self, M, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        # dijstra
        # node: (sum, a comb of index from each row), bounded by n ^ m 
        # edge: seq1 & seq2 only 1 idx diff, weight M[i][seq2[i]] - M[i][seq1[i]], bounded by mn
        # O(ElogV) = O(m^2nlogn) ?
        
        # O(m klogk)/ O(mk)
        m, n = len(M), len(M[0])
        res, seen = 0, set()
        hq = [(sum(x[0] for x in M), [0] * m)] # (sum of each row, index list w/ len of m)
        heapq.heapify(hq)
        
        while k:
            s, idx_ls = heapq.heappop(hq)
            res = s
            k -= 1
            for i in range(m):
                new_idx_ls = idx_ls[:]
                new_idx_ls[i] += 1 # test row by row and find min
                if new_idx_ls[i] < n and tuple(new_idx_ls) not in seen:
                    seen.add(tuple(new_idx_ls))
                    heapq.heappush(hq, (s + M[i][new_idx_ls[i]] - M[i][new_idx_ls[i] - 1], new_idx_ls))
        return res


class Solution_dp:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # DP, `dp[0]` maintain the `k smallest array sum` in `mat[:1]`.
        # It is possible that `k > len(mat[0])`. 
        # If so, `dp[0]` can only maintain the `len(mat[0]) smallest array sum` in `mat[:1]` at most.
        m, n = len(mat), len(mat[0])
        dp = mat[0][:min(k, n)]
        # print(dp)
        for row in mat[1:]:
            tmp = []
            # Compute the cross product between `dp[i-1]` and `mat[i]` for new pairs
            for i in dp:
                for j in row:
                    tmp += [i+j]
            dp = sorted(tmp)[:min(k, len(tmp))]
            # print(dp, len(dp)) # len(dp) = k in the loop
        return dp[-1]



class Solution_bs:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # Save all visited sums and corresponding indexes in a priority queue. 
        # Then, once you pop the smallest sum so far, you can quickly identify the next m candidates 
        # for smallest sum by incrementing each row index by 1.
        m, n = len(mat), len(mat[0])
        
        def countArraysHaveSumLessOrEqual(targetSum, r, sum, k):
            if sum > targetSum: return 0
            if r == m: return 1
            ans = 0
            for c in range(0, n):
                cnt = countArraysHaveSumLessOrEqual(targetSum, r + 1, sum + mat[r][c], k - ans)
                if cnt == 0: break
                ans += cnt
                if ans > k: break # prune when count > k
            return ans
        
        # binary search the target sum, 1 <= mat[i][j] <= 5000
        left, right, ans = m, m * 5000, -1
        while left < right:
            mid = left + (right - left) // 2
            cnt = countArraysHaveSumLessOrEqual(mid, 0, 0, k)
            if cnt >= k:
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans