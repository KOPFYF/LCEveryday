class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        '''
        if meet 0, end0 = end0 + end1
        if meet 1, end1 = end0 + end1 + 1
        '''
        # DP, buy/sell stock, O(n)/O(1)
        mod = 10**9 + 7
        end0, end1, cnt0 = 0, 0, 0 # [end with 0, end with 1]
        for i, b in enumerate(binary):
            
            if b == '1':
                end1 = (end0 + end1 + 1) % mod # +1 because single '1' could be a new soln
            else:
                end0 = (end0 + end1) % mod
                cnt0 = 1 # single '0'
            # print(end0, end1, cnt0)
        return (end0 + end1 + cnt0) % mod