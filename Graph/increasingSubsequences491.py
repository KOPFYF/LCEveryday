class Solution1_DP:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:  
        # pitfall: list is non-hashable so need to convert it to tuple of set
        n = len(nums)
        if not n: return []
        
        seqs = self.dfs(nums, n - 1, {})
        res = [seq for seq in seqs if len(seq) > 1]
        return res
    
    def dfs(self, nums, end, memo):
        if end in memo: return memo[end]
        
        if end == 0: # base case using nums[0]
            memo[end] = set([(nums[end], )])
            return memo[end]
        
        sub_seqs = self.dfs(nums, end - 1, memo) # use last state
        seqs = set([(nums[end],)]) # dont use last state
        for sub_seq in sub_seqs:
            if sub_seq[-1] <= nums[end]:
                seq = sub_seq + (nums[end],)
                # print(seq)
                seqs.add(seq)
        memo[end] = seqs.union(sub_seqs)
        return memo[end]


class Solution2_global_set(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/increasing-subsequences/discuss/97130/Java-20-lines-backtracking-solution-using-set-beats-100./101617
        # global dedup vs local dedup
        res = set()
        self.dfs(nums, 0, res, (), set())
        return res
    
    def dfs(self, nums, i, res, path, seen):
        if len(path) >= 2:
            res.add(path[:])
        if path not in seen:
            seen.add(path)
            for j in range(i, len(nums)):
                if not path or path[-1] <= nums[j]:
                    self.dfs(nums, j + 1, res, path + (nums[j],), seen)


class Solution3_localset(object):
    # This one should be the best, it prunes before 
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # https://leetcode.com/problems/increasing-subsequences/discuss/97130/Java-20-lines-backtracking-solution-using-set-beats-100./101617
        # global dedup vs local dedup
        res = set()
        self.dfs(nums, 0, res, ())
        return res
    
    def dfs(self, nums, i, res, path):
        
        if len(path) >= 2:
            res.add(path[:])
        seen = set()

        for j in range(i, len(nums)):
            if nums[j] not in seen:
                seen.add(nums[j])
                if not path or path[-1] <= nums[j]:
                    self.dfs(nums, j + 1, res, path + (nums[j],))

