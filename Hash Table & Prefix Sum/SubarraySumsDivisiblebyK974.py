class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix_sum = 0
        res = 0
        for a in A:
            prefix_sum += a
            res += d[prefix_sum % K]
            d[prefix_sum % K] += 1
        return res