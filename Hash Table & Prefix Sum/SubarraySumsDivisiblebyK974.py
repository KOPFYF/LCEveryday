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
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Time O(n), Space O(k)
        dic = defaultdict(int)
        dic[0] = 1
        res, rumsum = 0, 0
        for num in nums:
            rumsum += num
            res += dic[rumsum % k]
            dic[rumsum % k] += 1
        
        return res