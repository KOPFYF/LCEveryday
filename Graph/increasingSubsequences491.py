class Solution:
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