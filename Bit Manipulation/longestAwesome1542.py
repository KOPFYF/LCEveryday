class Solution:
    def longestAwesome(self, s: str) -> int:
        # bit mask + prefix + hash table O(10^n)/O(2^10)
        # bit mask all 10 digits, and find pattern through hashmap/dp memo
        # From left to right, use bitwise xor-operation to compute for any prefix the number of times modulo 2 of each digit. (mask ^= (1<<(s[i]-'0')).
        
        mask, res, full_mask = 0, 0, (1 << 10) - 1 
        dp = [-1] + [float('inf')] * full_mask
        for i in range(len(s)):
            mask ^= 1 << (ord(s[i]) - ord('0'))
            res = max(res, i - dp[mask]) # init
            for j in range(10):
                # flip an arbitrary bit mask ^ ( 1 << j)
                res = max(res, i - dp[mask ^ ( 1 << j)])
            dp[mask] = min(dp[mask], i)
        return res