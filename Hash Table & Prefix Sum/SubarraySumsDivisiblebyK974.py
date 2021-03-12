class Solution0:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        s, cnt = 0, 0
        for a in A:
            s += a
            mod = s % K
            # if mod < 0: 
            #     mod += K
            if mod in d:
                cnt += d[mod]
            d[mod] += 1
        return cnt

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