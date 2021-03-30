'''
1. Use 2-pointers algorithm to make sure all amount of characters outside the 2 pointers are smaller or equal to n/4.
2. That means you need to count the amount of each letter and make sure the amount is enough.
'''
class Solution:
    def balancedString(self, s: str) -> int:
        n, cnt = len(s), collections.Counter(s)
        i, res = 0, n
        for j in range(n):
            cnt[s[j]] -= 1
            while i < n and all(cnt[ch] <= n // 4 for ch in "QWER"):
                # while no char overflow, move left pointer
                res = min(res, j - i + 1)
                cnt[s[i]] += 1
                i += 1
        return res