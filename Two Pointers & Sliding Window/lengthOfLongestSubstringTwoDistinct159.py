class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        i = res = 0
        k = 2
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            while len(d.keys()) > k:
                d[s[i]] -= 1
                if d[s[i]] == 0: 
                    del d[s[i]]
                i += 1  
            res = max(res, j - i + 1)  
        return res


class Solution2(object):
    def lengthOfLongestSubstringTwoDistinct(self, A):
        # Time O(N), Space O(N)
        K = 2
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: 
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: 
                    K += 1
                i += 1
            res = max(res, j - i + 1)
        return res