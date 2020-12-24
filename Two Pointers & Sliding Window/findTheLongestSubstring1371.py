class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Bit mask & hash map
        mask = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        d, n, res = {0: -1}, 0, 0
        for i, c in enumerate(s):
            if c in mask:
                # XOR, 4a, 3e, 2i, 1o, 0u would be 01010
                # n would be 0 if count is even
                n ^= mask[c] 
            if n not in d:
                d[n] = i # the latest index for bit pattern n
            else:
                res = max(res, i - d[n]) # retrieve last seen pattern
            # print(bin(n)[2:], n, i, d, r)
        return res

        cnt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        i = res = 0
        for j in range(len(s)):
            if s[j] not in 'aenou':
                continue
            while any(v % 2 for v in cnt.values()):
                if s[i] in 'aeiou':
                    cnt[s[i]] -= 1
                i += 1
            cnt[s[j]] += 1
            res = max(res, j - i + 1)
            print(cnt, i, j, s[j])
        return res