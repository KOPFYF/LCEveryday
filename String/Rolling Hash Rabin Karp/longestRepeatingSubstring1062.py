class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        base = 26
        # mod = 10 ** 9 + 7
        
        def check(L):
            hashsum = 0
            for i in range(L):
                hashsum = (hashsum * base + nums[i])
            seen = {hashsum}
            power = pow(base, L)
            for j in range(1, n - L + 1):
                hashsum = (hashsum * base - nums[j - 1] * power + nums[j + L - 1])
                if hashsum in seen:
                    return True
                seen.add(hashsum)
            return False
        
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1