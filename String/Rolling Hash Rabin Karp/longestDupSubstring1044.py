class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        base = 26
        mod = 10 ** 9 + 7
        
        def check(L):
            hashsum = 0
            for i in range(L):
                hashsum = (hashsum * base + nums[i])
            seen = {hashsum}
            power = pow(base, L)
            for j in range(1, n - L + 1):
                hashsum = (hashsum * base - nums[j - 1] * power + nums[j + L - 1])
                if hashsum in seen:
                    return j
                seen.add(hashsum)
            return -1
        
        l, r, k = 1, n, 0
        while l < r:
            mid = (l + r) // 2
            start = check(mid)
            if start != -1:
                l = mid + 1
                k = start
            else:
                r = mid
        # print(l, r, mid, k)
        return S[k: k + l - 1]