class Solution:
    def countPairs(self, A: List[int]) -> int:
        # O(N)/O(N)
        mod = 10 ** 9 + 7
        res = 0
        count = collections.defaultdict(int)
        for num in A: 
            for k in range(22):
                res += count[2**k - num]
            count[num] += 1
        return res % mod
    
class Solution2:
    def countPairs(self, A: List[int]) -> int:    
        def isPower2(n):
            return (n & (n-1) == 0) and n != 0       

        power2s = [2 ** i for i in range(0, 22)]
        mod = 10**9 + 7
        cnt = Counter(A)

        res = 0
        seen = set()
        for d in sorted(cnt.keys()):
            if isPower2(2 * d) and (d, d) not in seen:
                seen.add((d, d))
                res += cnt[d] * (cnt[d] - 1) // 2

            for power2 in power2s:
                if power2 - d in cnt and (d, power2 - d) not in seen:
                    seen.add((d, power2 - d))
                    seen.add((power2 - d, d))
                    res += cnt[d] * cnt[power2 - d]

        return res % mod

                